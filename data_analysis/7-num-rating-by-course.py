import justpy as jp
import pandas
from datetime import datetime
from pytz import utc

data = pandas.read_csv('./resources/reviews.csv', parse_dates=['Timestamp'])
share = data.groupby(['Course Name'])['Rating'].count()

chart_def = """
{
    chart: {
        plotBackgroundColor: null,
        plotBorderWidth: null,
        plotShadow: false,
        type: 'pie'
    },
    title: {
        text: 'Number of rating by course'
    },
    tooltip: {
        pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
    },
    accessibility: {
        point: {
            valueSuffix: '%'
        }
    },
    plotOptions: {
        pie: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: {
                enabled: true,
                format: '<b>{point.name}</b>: {point.percentage:.1f} %'
            }
        }
    },
    series: [{
        name: 'Courses',
        colorByPoint: true,
        data: []
    }]
}
"""

def app():
    wp = jp.WebPage()
    h1 = jp.QDiv(a=wp, text='Analysis of Course Reviews', classes='text-h3 text-center q-pa-md')
    p1 = jp.QDiv(a=wp, text='There graphs represent course review analysis')
    hc = jp.HighCharts(a=wp, classes='m-2 p-2 border', options=chart_def)

    hc_data = [{'name': course_name, 'y': rating} for course_name, rating in list(zip(share.index, share))]
    hc.options.series[0].data = hc_data

    return wp

jp.justpy(func=app)
