import csv

from datetime import datetime
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'data/fire_data_1d.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    latitude, longitude, frp = [], [], []
    for row in reader:
        lon = float(row[1])
        lat = float(row[0])
        fr = float(row[11])
        longitude.append(lon)
        latitude.append(lat)
        frp.append(fr)

    #data = [Scattergeo(lat=latitude, lon=longitude)]
    data = [{
    'type':'scattergeo',
    'lat': latitude,
    'lon': longitude,
    'marker':{
            'color': frp,
            'colorscale': 'Electric',
            'reversescale': True,
            'colorbar': {'title': 'Fire'},
    },
}]
    my_layout = Layout(title='Global Fire Map!')

    fig = {'data': data, 'layout': my_layout}
    offline.plot(fig, filename='global_fire_data.html')
