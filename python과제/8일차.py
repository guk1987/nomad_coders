import requests
from flask import Flask, render_template, request

base_url = "http://hn.algolia.com/api/v1"

# This URL gets the newest stories.
new = f"{base_url}/search_by_date?tags=story"

# This URL gets the most popular stories
popular = f"{base_url}/search?tags=story"


# This function makes the URL to get the detail of a storie by id.
# Heres the documentation: https://hn.algolia.com/api
def make_detail_url(id):
    return f"{base_url}/items/{id}"


db = {}
app = Flask("DayNine")


@app.route("/")
def home(new):
    r_new = requests.get(new)
    new_news = r_new.json()
    print(new_news)
    return render_template('home.html', new_news=new_news)


app.run()

r_new = requests.get(new)
# dict_keys(['hits', 'nbHits', 'page', 'nbPages', 'hitsPerPage', 'exhaustiveNbHits', 'exhaustiveTypo', 'query', 'params', 'renderingContent', 'processingTimeMS'])
r_new.json().keys()



r_popular = requests.get(popular)
#dict_keys(['hits', 'nbHits', 'page', 'nbPages', 'hitsPerPage', 'exhaustiveNbHits', 'exhaustiveTypo', 'query', 'params', 'renderingContent', 'processingTimeMS'])
r_popular.json().keys()

#dict_keys(['created_at', 'title', 'url', 'author', 'points', 'story_text', 'comment_text', 'num_comments', 'story_id', 'story_title', 'story_url', 'parent_id', 'created_at_i', '_tags', 'objectID', '_highlightResult'])
r_popular.json()['hits'][0]['created_at']
r_popular.json()['hits'][0]['title']  #제목
r_popular.json()['hits'][0]['url']  #괄호 안에 오는거
r_popular.json()['hits'][0]['points']  #포인트

r_popular.json()['hits'][0]['num_comments']  # 코멘트
r_popular.json()['hits'][0]['author']  # 작성자
r_popular.json()['hits'][0]['objectID']  # ID -> 이걸로 페이지 연결하고,
#이걸로 children 검색하자

id = '16582136'
id_get = requests.get(f"{base_url}/items/{id}")

#dict_keys(['id', 'created_at', 'created_at_i', 'type', 'author', 'title', 'url', 'text', 'points', 'parent_id', 'story_id', 'children', 'options'])
id_get.json().keys()

#{'id': 16582400, 'created_at': '2018-03-14T04:43:36.000Z', 'created_at_i': 1521002616, 'type': 'comment', 'author': None, 'title':
#None, 'url': None, 'text': None, 'points': None, 'parent_id': 16582136, 'story_id': 16582136, 'children': [], 'options': []}
id_get.json()['children'][0]  # 'author' 가 None이면 "[deleted]"를 출력하자..

id_get.json()['children'][1]['author']  # 작성자
id_get.json()['children'][1]['text']  # 내용
