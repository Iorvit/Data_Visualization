import requests

from plotly import offline
from plotly.graph_objs import Bar

name_language = 'python'
# Создание вывода API и сохранение ответа.
url = f'https://api.github.com/search/repositories?q=language:{name_language}'
f'&soet=stars'
headers = {'Accept': 'applecation/vnd.github.v3+json'}
r = requests.get(url, headers=headers)

# Обработка результатов.
response_dict = r.json()
repo_dicts = response_dict['items']
repo_links, stars, labels =[], [], []
for repo_dict in repo_dicts:
    stars.append(repo_dict['stargazers_count'])
    labels.append(f"{repo_dict['owner']['login']}"
        f"<br />{repo_dict['description']}")
    repo_links.append(f"<a href='{repo_dict['html_url']}'>"
        f"{repo_dict['name']}</a>")

# Построение визуализации.
data = [{
    'type': 'bar',
    'x': repo_links,
    'y': stars,
    'hovertext': labels,
    'marker': {
    'color': 'rgb(60, 100, 150)',
    'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6,
}]

my_layout = {
        'title': f'Most-Starred {name_language} Projects on GitHub',
        'titlefont': {'size': 28},
        'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
        },
        'yaxis': {
        'title': 'Stars',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
        },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')
    

