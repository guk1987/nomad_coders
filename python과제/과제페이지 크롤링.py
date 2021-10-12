# import requests
# from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import os

# headless_options = webdriver.ChromeOptions()
# headless_options.add_argument('headless')
# headless_options.add_argument('window-size=1920x1080')
# headless_options.add_argument('disable-gpu')
# headless_options.add_argument(
#     'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36')
# options = webdriver.ChromeOptions()
# options.add_argument('disable-infobars')
# options.add_argument("User-Agent={유저 에이전트}")
# options.add_argument('--user-data-dir={사용자 환경설정 경로}')  # 추가
# driver = webdriver.Remote('http://localhost:4444/wd/hub',
#                           options.to_capabilities())  # 셀레 서버를 Standalone 방식으로 가동
# driver.get('https://nid.naver.com/nidlogin.login')
# # 크롬에 저장된 로그인 정보 가져오는 시간 벌어주는 용도 (10 ~ 15초)
# driver.implicitly_wait(random.randrange(10, 16))
# driver.find_element_by_css_selector("#frmNIDLogin > fieldset > input").click()
# # WEB OTP 싸이트 접속
# driver = webdriver.Chrome(
#     'python과제\chromedriver.exe')  # , options=headless_options)
# driver.get('https://nomadcoders.co/c/python-challenge/lobby')
# input('')


# r = requests.get(url)
# r_soup = BeautifulSoup(r.text, 'html.parser')

link = 'naver.com'
if 'http://' and 'https://' not in link:
    link = 'https://' + link
    print(link)
elif '.com' not in link:
    print(f'{link} is not a valid.')


test_list = [1, 2, 3, 4]

print(bool(1 in test_list))
print(bool(1 or 5 not in test_list))
print(bool(1 not in test_list or 5 not in test_list))
print(bool(1 in test_list and 2 in test_list))
