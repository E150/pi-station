import datetime
import plotly.plotly as plotly
import plotly.graph_objs as go

PLOTLY_USER = 'YOUR_USER'
PLOTLY_API_KEY = 'YOUR_API_KEY'


def scatter(datetimes, sys_tmps, ds_tmps, dht_hums, dht_tmps, bmp_tmps, bmp_prss, bmp_alts, bmp_slps):
 
    print 'Log in to Plot.ly as user {0}...'.format(PLOTLY_USER)
    plotly.sign_in(PLOTLY_USER, PLOTLY_API_KEY)
    # Create traces
    trace0 = go.Scatter(  # @UndefinedVariable
        x = datetimes,
        y = sys_tmps,
        mode = 'markers',
        name = 'CPU Temp'
    )
    trace1 = go.Scatter(  # @UndefinedVariable
        x = datetimes,
        y = ds_tmps,
        mode = 'markers',
        name = 'DS Temp'
    )
    trace2 = go.Scatter(  # @UndefinedVariable
        x = datetimes,
        y = dht_hums,
        mode = 'markers',
        name = 'Humidity'
    )
    trace3 = go.Scatter(  # @UndefinedVariable
        x = datetimes,
        y = dht_tmps,
        mode = 'markers',
        name = 'DHT Temp'
    )
    trace4 = go.Scatter(  # @UndefinedVariable
        x = datetimes,
        y = bmp_tmps,
        mode = 'markers',
        name = 'Temp'
    )
    trace5 = go.Scatter(  # @UndefinedVariable
        x = datetimes,
        y = bmp_prss,
        mode = 'lines',
        name = 'Pressure'
    )
    trace6 = go.Scatter(  # @UnusedVariable @UndefinedVariable
        x = datetimes,
        y = bmp_alts,
        mode = 'markers',
        name = 'Altitude'
    )
    trace7 = go.Scatter(  # @UndefinedVariable
        x = datetimes,
        y = bmp_slps,
        mode = 'lines',
        name = 'Sea Level Pressure'
    )
    temp = [trace0, trace1, trace3, trace4]
    humi = [trace2]
    pres = [trace5, trace7]
    print 'Uploading data to Plot.ly...'
    plotly.plot(temp, filename='Temperatures', auto_open=False)
    plotly.plot(humi, filename='Humidity', auto_open=False)
    plotly.plot(pres, filename='Pressure', auto_open=False)
    return None

def upload(dump):

    datetimes = []
    sys_tmps = []
    ds_tmps = []
    dht_hums = []
    dht_tmps = []
    bmp_tmps = []
    bmp_prss = []
    bmp_alts = []
    bmp_slps = []
    
    for row in dump:
        datetimes.append(datetime.datetime.fromtimestamp(row[1]).strftime('%Y-%m-%d %H:%M:%S'))
        sys_tmps.append(row[2])
        ds_tmps.append(row[3])
        dht_hums.append(row[4])
        dht_tmps.append(row[5])
        bmp_tmps.append(row[6])
        bmp_prss.append(row[7])
        bmp_alts.append(row[8])
        bmp_slps.append(row[9])

    scatter(datetimes, sys_tmps, ds_tmps, dht_hums, dht_tmps, bmp_tmps, bmp_prss, bmp_alts, bmp_slps)
    return None

