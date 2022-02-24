from operator import itemgetter
from plotly import offline
from plotly.graph_objs import Bar

import requests

# Создание вызова API и сохранение ответа.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Обработка информации о каждой статье.
submission_ids = r.json()
print(submission_ids)
submission_dicts = []
titles_st, commets_st, repo_links  = [], [], []
for submission_id in submission_ids[:10]:
    # Создание отдельного вызова API для каждого вызова статьи.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()
    m = f"https://news.ycombinator.com/item?id={submission_id}"
    # Постороение словаря для каждой статьи.
    try:
        submission_dict = {
            'title': response_dict['title'],
            'hn_link': m,
            'comments': response_dict['descendants']
        }
    except KeyError:
        continue
    else:

        submission_dicts.append(submission_dict)
        titles_st.append(f"<a href='{m}'>{response_dict['title']}</a>")
        commets_st.append(response_dict['descendants'])

commets_st = sorted(commets_st, reverse=True)
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                            reverse=True)

for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")

data = [{
    'type': 'bar',
    'x': titles_st,
    'y': commets_st,

}]

my_layout = {
        'title': f'Most-Starred comments Projects on Hecker_news',
        'titlefont': {'size': 28},
        'xaxis': {
        'title': 'Name Projects',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
        },
        'yaxis': {
        'title': 'N comments',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
        },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_reposs.html')
