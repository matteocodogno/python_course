import folium
import pandas


def color_meter(m: int) -> str:
    if m < 1000:
        return 'green'
    elif 1000 <= m < 3000:
        return 'orange'
    else:
        return 'red'


world_map = folium.Map(location=[38.41404508672903, -98.51618078050954], zoom_start=6, tiles='cartodb positron')

df = pandas.read_csv('resources/Volcanoes.txt')

# sub_df = df.loc[:, 'LAT':'LON']
# points = list(sub_df.itertuples(index=False, name=None))

# how to add marker to map
volcanoes = folium.FeatureGroup(name="Volcanoes")

# Add markers to the Map
lat = list(df['LAT'])
lon = list(df['LON'])
elev = list(df['ELEV'])
for lt, ln, el in zip(lat, lon, elev):
    volcanoes.add_child(folium.CircleMarker(location=(lt, ln), radius=6, fill=True, popup=f'{el} m', color=color_meter(el)))
world_map.add_child(volcanoes)

population = folium.FeatureGroup(name="Population")
# Add polygon based on geospatial json
population.add_child(folium.GeoJson(data=open('./resources/world.json', 'r', encoding='utf-8-sig').read(),
    style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000
    else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))


world_map.add_child(population)
world_map.add_child(folium.LayerControl())

# Generate the map
world_map.save('map.html')
