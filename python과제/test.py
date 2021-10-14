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


r_new = requests.get(new)
# dict_keys(['hits', 'nbHits', 'page', 'nbPages', 'hitsPerPage', 'exhaustiveNbHits', 'exhaustiveTypo', 'query', 'params', 'renderingContent', 'processingTimeMS'])
r_new.json().keys()

db = r_new.json()

db['hits']

for item in db['hits']:
    print(type(item))
    item('title')

t_db = {}
