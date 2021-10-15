import requests
from flask import Flask, render_template, request
from bs4 import BeautifulSoup


"""
When you try to scrape reddit make sure to send the 'headers' on your request.
Reddit blocks scrappers so we have to include these headers to make reddit think
that we are a normal computer and not a python script.
How to use: requests.get(url, headers=headers)
"""


"""
All subreddits have the same url:
i.e : https://reddit.com/r/javascript
You can add more subreddits to the list, just make sure they exist.
To make a request, use this url:
https://www.reddit.com/r/{subreddit}/top/?t=month
This will give you the top posts in per month.
"""

# subreddits = [
#     "javascript",
#     "reactjs",
#     "reactnative",
#     "programming",
#     "css",
#     "golang",
#     "flutter",
#     "rust",
#     "django"
# ]


def get_result_list(_subreddits, _final_restul_l):
    redit_url = 'https://reddit.com/r/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}

    result_l = []
    search_max = 4

    for subreddit in _subreddits:
        url = redit_url + subreddit + '/top/?t=month'
        r = requests.get(url, headers=headers, verify=False)
        r_suop = BeautifulSoup(r.text, 'html.parser')

        items = r_suop.find_all('div', {'data-testid': 'post-container'})

        for item in items:
            item_l = []
            item_l.append(subreddit)    # 0: 어디 게시판인가
            try:
                item_l.append(
                    item.find('a', 'SQnoC3ObvgnGjWt90zD9Z _2INHSNB8V5eaWp4P0rY_mE').get_text())  # 1: 타이틀
                item_l.append(
                    url +
                    item.find('a', 'SQnoC3ObvgnGjWt90zD9Z _2INHSNB8V5eaWp4P0rY_mE').get('href'))  # 2: url
                item_l.append(
                    item.find('div', '_1rZYMD_4xY3gRcSS3p8ODO _3a2ZHWaih05DgAOtvu6cIo').get_text())  # 3: upvote
                result_l.append(item_l)
            except:
                pass  # 값에 None Type이 있을 경우에는 list에 넣지 않고 Pass 한다.

            if len(result_l) == search_max:
                _final_restul_l += result_l
                result_l = []
                break

    return _final_restul_l


subreddits = ['css', 'reactjs']
final_restul_l = []
final_restul_l = get_result_list(subreddits, final_restul_l)

print(len(final_restul_l))
print(final_restul_l)
# r_suop.get_text()
# item = r_suop.find('a', 'SQnoC3ObvgnGjWt90zD9Z _2INHSNB8V5eaWp4P0rY_mE')
# item_title = item.get_text()  # 제목
# # url 주소 /r/Python/comments/priqp7/any_love_for_python_25_on_an_i486/
# item_url = item.get('href')

# item_upvote = item.find(
#     'div', "_1rZYMD_4xY3gRcSS3p8ODO _3a2ZHWaih05DgAOtvu6cIo")

# item_upvote = '15'

# if 'k' in item_upvote:
#     item_upvote = item_upvote.replace("k", "")
#     item_upvote = float(item_upvote) * 1000
# else:
#     item_upvote = float(item_upvote)

# print(f'{type(item_upvote)} : {item_upvote}')

# app = Flask("DayEleven")


# app.run(host="0.0.0.0")


# test_dict = {'python':
#              [{'title': 'abc',
#               'url': 'https://naver.com',
#                'upvote': 2100.0},
#               {'title': 'bbc',
#               'url': 'https://yahoo.com',
#                'upvote': 15}
#               ],
#              'java': [{'title': 'java - abc',
#                        'url': 'https://java-naver.com',
#                       'upvote': 2100.0},
#                       {'title': 'bbc',
#                       'url': 'https://java-yahoo.com',
#                        'upvote': 15}
#                       ]

#              }
# sorted(test_dict.values(), key=lambda title: title)


# student_tuples = [
#     ['john', 'A', 15],
#     ['jane', 'B', 12],
#     ['dave', 'B', 10],
# ]
# sorted(student_tuples, key=lambda student: student[2], reverse=True)
