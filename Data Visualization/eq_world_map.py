import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline
from plotly import colors 

"""for key in colors.PLOTLY_SCALES.keys():
    print(key)"""

# Изучение структуры данных.
filename = 'data/7erch.json'
with open(filename, encoding='utf-8') as f:
    all_eq_data = json.load(f)

# Создаёт файл в более удобочитаймом фомате.
"""readable_file = 'data/readable_eq_data.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)"""

all_eq_dicts = all_eq_data['features']
#Заголовок графика из файла.
title = all_eq_data['metadata']['title']
mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    hover_texts.append(eq_dict['properties']['title'])
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])

# Нанесение данных на карту.
data = [{
    'type':'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker':{
            'size': [5*mag for mag in mags],
            'color': mags,
            'colorscale': 'Electric',
            'reversescale': True,
            'colorbar': {'title': 'Magnitude'},
    },
}]

my_layout = Layout(title=title)

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')

