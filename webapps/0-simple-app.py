from matplotlib.pyplot import text
import justpy as jp
import pandas
from datetime import datetime
from pytz import utc

data = pandas.read_csv('../reviews.csv', parse_dates=['Timestamp'])

chart_def = """
{
        chart: {
            type: 'bar'
        },
        title: {
            text: 'Fruit Consumption'
        },
        xAxis: {
            categories: ['Apples', 'Bananas', 'Oranges']
        },
        yAxis: {
            title: {
                text: 'Fruit eaten'
            }
        },
        series: [{
            name: 'Jane',
            data: [1, 0, 4]
        }]
}

"""


def app():
    web_page = jp.QuasarPage()

    h1 = jp.QDiv(a=web_page, text='Analysis of Courses Reviews',
                 classes='text-h1')
    p1 = jp.QDiv(
        a=web_page, text='These graphs represent course review analysis')

    data['Week'] = data['Timestamp'].dt.strftime('%Y-%U')

    week_average = data.groupby(['Week']).mean()

    high_charts = jp.HighCharts(a=web_page, options=chart_def)
    # high_charts.options = chart_def

    high_charts.options.xAxis.categories = list(zip(week_average.index))
    high_charts.options.series[0].data = list(zip(week_average['Rating']))

    return web_page


jp.justpy(app)
