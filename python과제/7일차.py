import os
import csv
import requests
from bs4 import BeautifulSoup


def get_jobs_url():

    alba_url = "http://www.alba.co.kr"
    r = requests.get(alba_url)
    r_suop = BeautifulSoup(r.text, 'html.parser')
    superjobs = r_suop.find_all('ul', 'goodsBox')

    # superjobs[0] = 슈퍼 채용정보
    # superjobs[1] = 슈퍼 브랜드 채용정보
    # superjobs[2] = 그랜드 채용 정보
    # superjobs[3] = 긴급 채용 정보

    data_li = superjobs[1].find_all('li', 'impact')

    company_keys = []
    url_vals = []

    for item in data_li:
        company_name = item.find('span', 'company')
        company_keys.append(company_name.get_text())

        company_url = item.find('a', 'goodsBox-info')
        url_vals.append(company_url.get("href"))

    company_name_url_dict = dict(zip(company_keys, url_vals))

    return company_name_url_dict


def get_detail_jobs(company_name_url_dict):
    # company_detail_dict = {'근무지':[], ''}

    for item_key, item_val in company_name_url_dict.items():
        # CSO 저장을 위한 회사명 -> CSV 파일명 전처리
        csv_file_name = item_key.replace('/', '_')
        # print(csv_file_name, item_val)

        job_locals = []
        job_names = []
        job_times = []
        job_pays = []
        job_rgdates = []
        # page = 1

        r = requests.get(f'{item_val}job/brand/?page=1&pagesize=1000')
        r_soup = BeautifulSoup(r.text, 'html.parser')
        job_table = r_soup.find('table')

        try:

            locals = job_table.find_all('td', 'local first')
            for local in locals:
                job_locals.append(
                    local.get_text().strip().replace('\xa0', ' '))

            names = job_table.find_all('span', 'company')
            for name in names:
                job_names.append(name.get_text().strip())

            times = job_table.find_all('td', 'data')
            for time in times:
                job_times.append(time.get_text().strip())

            pays = job_table.find_all('span', 'number')
            for pay in pays:
                job_pays.append(pay.get_text().strip())

            rgdates = job_table.find_all('td', 'regDate last')
            for rgdate in rgdates:
                job_rgdates.append(rgdate.get_text().strip())
        except:
            pass

        writhe_to_csv(csv_file_name, job_locals, job_names,
                      job_times, job_pays, job_rgdates)


def writhe_to_csv(csv_file_name, job_locals, job_names, job_times, job_pays, job_rgdates):

    file = open(f'{csv_file_name}.csv', mode='w', newline='')
    write = csv.writer(file)
    write.writerow(['local', 'company', 'time', 'pay', 'rgdate'])

    for item in job_locals:
        l_index = job_locals.index(item)
        write.writerow([item, job_names[l_index], job_times[l_index],
                        job_pays[l_index], job_rgdates[l_index]])

    file.close()
    print(f'{csv_file_name} CSV 저장 완료!')


if __name__ == '__main__':

    os.system("cls")

    company_name_url_dict = get_jobs_url()
    get_detail_jobs(company_name_url_dict)

    print('완료되었습니다!')

    # writhe_to_csv(csv_file_name, job_locals, job_names,
    #               job_times, job_pays, job_rgdates)
