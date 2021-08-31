import justpy as jp
import pandas
from datetime import datetime
from pytz import utc

data = pandas.read_csv('./resources/reviews.csv', parse_dates=['Timestamp'])
data['Month'] = data['Timestamp'].dt.strftime('%Y-%m')
month_course_average = data.groupby(['Month', 'Course Name'])['Rating'].mean().unstack()

chart_def = """
{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Average Rating by Day'
    },
    subtitle: {
        text: 'According to the Standard Atmosphere Model'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Date'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: 0 to 80 km.'
        },
        maxPadding: 0.05,
        showLastLabel: true,
    },
    yAxis: {
        title: {
            text: 'Average Rating'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: -90°C to 20°C.'
        },
        lineWidth: 2
    },
    legend: {
        enabled: true,
        floating: false,
        borderWidth: 1,
        backgroundColod: '#FFFFFF'
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.x} {point.y}'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Average Rating',
        data: []
    }]
}
"""

def app():
    wp = jp.WebPage()
    h1 = jp.QDiv(a=wp, text='Analysis of Course Reviews', classes='text-h3 text-center q-pa-md')
    p1 = jp.QDiv(a=wp, text='There graphs represent course review analysis')
    hc = jp.HighCharts(a=wp, classes='m-2 p-2 border', options=chart_def)

    hc.options.xAxis.categories = list(month_course_average.index)
    hc_data = [{'name': course_name, 'data': [rating for rating in month_course_average[course_name]]} for course_name in month_course_average.columns]
    hc.options.series = hc_data

    return wp

jp.justpy(func=app)
