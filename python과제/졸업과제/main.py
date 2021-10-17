"""
These are the URLs that will give you remote jobs for the word 'python'

https://stackoverflow.com/jobs?r=true&q=python
https://weworkremotely.com/remote-jobs/search?term=python
https://remoteok.io/remote-dev+python-jobs

Good luck!
"""

import requests
from flask import Flask, render_template, request, send_file
from bs4 import BeautifulSoup
from werkzeug.utils import redirect
import csv

#fake_db / app 선언
fake_db = {}
app = Flask("졸업")


#fake_db에 검색어가 없으면 True를 반환한다.
def check_first_search(_search_text):
    _check = not bool(_search_text in fake_db.keys())
    return _check


# 각 게시물마다 추출한 자료를 fake_db에 업데이트한다.
def update_dict(_search_text, _title, _company, _url):
    _set_dict = {'title': _title, 'company': _company, 'url': _url}
    fake_db.get(_search_text).append(_set_dict)


#02 검색어를 입력 받는다.
# search_text = 'python'

#03-01 참 : 크롤링을 시작하여 fake_db에 추가한다.
#03-01-01 f'https://stackoverflow.com/jobs?r=true&q={search_text}' 크롤링


# url을 넣고 soup 반환
def get_soup(_url):
    headers = {
        'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
    }
    _r = requests.get(_url, headers=headers)

    return BeautifulSoup(_r.text, 'html.parser')


# soup를 넣고 Max page를 반환
def get_max_page_in_sof(_soup):
    try:
        _pages = _soup.find('div', {
            'class': 's-pagination'
        }).find('a').get('title')
        _pages = _pages.strip().split(' ')
        _max_page = int(_pages[-1])
        return _max_page
    except:
        return 1


# 검색어를 넣고 스택 오버 플로우 스크랩핑
def stackoverflow_scrapper(search_text):
    #스크랩핑 : Max page를 구해온다.
    url = f'https://stackoverflow.com/jobs?r=true&q={search_text}&sort=p'
    stackoverflow_soup = get_soup(url)  #soup 가져오기
    max_page = get_max_page_in_sof(stackoverflow_soup)  # max_page 찾기

    #스크랩핑 : 각 페이지마다 제목/회사/url을 구해서 Fake_db를 업데이트한다.
    for page in range(1, max_page + 1):
        url = f'https://stackoverflow.com/jobs?q={search_text}&r=true&pg={page}&sort=p'
        stackoverflow_soup = get_soup(url)
        jobs = stackoverflow_soup.find_all('div', {'data-jobid': not None})

        for job in jobs:

            job_title = job.find('a', 's-link stretched-link').get_text()
            job_title = job_title.strip().replace('/n', '')
            job_url = job.get('data-result-id')
            job_url = f'https://stackoverflow.com/jobs/{job_url}'
            job_company = job.find(
                'h3',
                'fc-black-700 fs-body1 mb4').find('span').get_text().strip()

            ###########################테스트 코드################################
            # d_ago = job.find(
            #     'ul', 'mt4 fs-caption fc-black-500 horizontal-list').find(
            #         'span').get_text()
            # print(f'{page} : {d_ago} : {job_title}\n{job_company}\n{job_url}')
            #####################################################################

            #Fake_DB 업데이트
            update_dict(search_text, job_title, job_company, job_url)
    return


def weworkremotely_scrapper(search_text):
    url = f'https://weworkremotely.com/remote-jobs/search?term={search_text}'
    wework_soup = get_soup(url)
    jobs = wework_soup.find_all('li', 'feature')

    for job in jobs:

        job_title = job.find('span', 'title').get_text().strip()
        job_company = job.find('span', 'company').get_text().strip()
        job_url = 'https://weworkremotely.com' + job.find_all('a')[1]['href']

        #테스트 코드
        # print(f'{job_company} : {job_title}\n {job_url}')

        #Fake_DB 업데이트
        update_dict(search_text, job_title, job_company, job_url)

    return


def remoteok_scrapper(search_text):
    url = f'https://remoteok.io/remote-dev+{search_text}-jobs'
    remoteok_soup = get_soup(url)
    jobs = remoteok_soup.find_all('td',
                                  'company position company_and_position')

    for job in jobs[1:]:  # jobs[1]에는 다른 값에 들어가 있음 건너뛰고 읽음
        job_title = job.find('h2', {'itemprop': 'title'}).get_text().strip()
        job_company = job.find('h3', {'itemprop': 'name'}).get_text().strip()
        job_url = 'https://remoteok.io' + job.find('a', {
            'class': 'preventLink',
            'itemprop': 'url'
        })['href']
        #Fake_DB 업데이트
        update_dict(search_text, job_title, job_company, job_url)

    return


def save_to_csv(jobs):
    file = open("jobs.csv", mode="w", newline="", encoding='utf-8')
    writer = csv.writer(file)
    writer.writerow(["title", "company", "link_url"])
    for job in jobs:
        writer.writerow(list(job.values()))
    return


@app.route('/')
def home():
    return render_template('졸업_index.html')


@app.route('/report')
def report():

    #검색어를 받는다
    search_text = request.args.get('search_text')

    if search_text:
        search_text = search_text.lower()

        #fake DB에 있는지 체크해서 없으면 크롤링 시작한다.
        if check_first_search(search_text):

            #Fake DB에 내용이 없으므로 해당 Search_text로 Key를 하나 생성한다.
            fake_db[search_text] = []

            #각 페이지 크롤링해서 title / company / url을 fake_db에 업데이트
            stackoverflow_scrapper(search_text)
            weworkremotely_scrapper(search_text)
            remoteok_scrapper(search_text)

        #해당 검색어는 이미 크롤링되어서 Fake DB에 있으므로 바로 결과 페이지로 넘어감
        else:
            print(f'이미 Fake DB에 등록되어있습니다. {fake_db.keys()}')
    else:
        return redirect('/')

    rst_num = len(fake_db[search_text])
    return render_template('졸업_report.html',
                           fake_db=fake_db,
                           search_text=search_text,
                           rst_num=rst_num)


@app.route('/export')
def export():
    search_text = request.args.get('search_text')
    if search_text:
        search_text = search_text.lower()
        jobs = fake_db[search_text]
        save_to_csv(jobs)

    else:
        return redirect('/')
    return send_file('jobs.csv')


app.run()