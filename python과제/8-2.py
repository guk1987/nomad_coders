import requests
from flask import Flask, render_template, request

base_url = "http://hn.algolia.com/api/v1"

# This URL gets the newest stories.
new = f"{base_url}/search_by_date?tags=story"

# This URL gets the most popular stories
popular = f"{base_url}/search?tags=story"


# global popular_db, new_db, comments_db
def make_detail_url(id):
    return f"{base_url}/items/{id}"


app = Flask("DayNine")

db = {}


@app.route("/")
def home():
    # print(f'popular_db : {bool(db['popular'])}')
    # print(f'new_db : {bool(db['new'])}')
    if 'popular' in db.keys():
        print('popular Fake DB가 존재합니다! PASS!')
        pass
    else:
        print('popular API 호출!')

        r_popular = requests.get(popular)
        db['popular'] = r_popular.json()

    order_by = request.args.get('order_by')
    if order_by == 'new':

        if 'new' in db.keys():
            print('new Fake DB가 존재합니다! PASS!')
            pass
        else:
            print('new API 호출!')

            r_new = requests.get(new)
            db['new'] = r_new.json()

        return render_template('order_new.html', items=db)

    # print(db['popular'])

    return render_template('index.html', items=db)


@app.route("/<id>")
def detail(id):
    if id in db.keys():
        print('해당 ID Fake DB가 존재합니다! PASS!')
        print(db[id].keys())
        print(db[id]['id'])
        print(db[id]['author'])
        print(db[id]['title'])
        print(db[id]['url'])
        print(db[id]['text'])
        print(db[id]['children'].keys())
        pass
    else:
        print('ID API 호출!')
        id_url = make_detail_url(id)
        r_id = requests.get(id_url)
        db[id] = r_id.json()
        print(db[id].keys())
        print(db[id]['author'])
        print(db[id]['title'])
        print(db[id]['url'])
        print(db[id]['text'])
        print(db[id]['children'].keys())
    return render_template('detail.html', items=db[id])


app.run(host='127.0.0.1')
