import justpy as jp
import pandas
from datetime import datetime
from pytz import utc

data = pandas.read_csv('./resources/reviews.csv', parse_dates=['Timestamp'])
data['Month'] = data['Timestamp'].dt.strftime('%Y-%m')
month_course_average = data.groupby(['Month', 'Course Name'])['Rating'].count().unstack()

chart_def = """
{

    chart: {
        type: 'streamgraph',
        marginBottom: 30,
        zoomType: 'x'
    },

    title: {
        floating: true,
        align: 'left',
        text: 'Course rating by month'
    },
    subtitle: {
        floating: true,
        align: 'left',
        y: 30,
        text: 'Source: <a href="https://www.sports-reference.com/olympics/winter/1924/">sports-reference.com</a>'
    },

    xAxis: {
        maxPadding: 0,
        type: 'category',
        crosshair: true,
        categories: [],
        labels: {
            align: 'left',
            reserveSpace: false,
            rotation: 270
        },
        lineWidth: 0,
        margin: 20,
        tickWidth: 0
    },

    yAxis: {
        visible: false,
        startOnTick: false,
        endOnTick: false
    },

    legend: {
        enabled: false
    },

    annotations: [{
        labels: [{
            point: {
                x: 5.5,
                xAxis: 0,
                y: 30,
                yAxis: 0
            },
            text: 'Course Launched'
        }, {
            point: {
                x: 18,
                xAxis: 0,
                y: 90,
                yAxis: 0
            },
            text: 'Python got popular'
        }],
        labelOptions: {
            backgroundColor: 'rgba(255,255,255,0.5)',
            borderColor: 'silver'
        }
    }],

    plotOptions: {
        series: {
            label: {
                minFontSize: 5,
                maxFontSize: 15,
                style: {
                    color: 'rgba(255,255,255,0.75)'
                }
            }
        }
    },

    series: [],

    exporting: {
        sourceWidth: 800,
        sourceHeight: 600
    }

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
