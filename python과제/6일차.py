import os
import requests
from bs4 import BeautifulSoup


def main():
    # os.system("clear")
    os.system("cls")
    print('Hello! please choose select a country by number:')
    url = "https://www.iban.com/currency-codes"
    r = requests.get(url)
    r_suop = BeautifulSoup(r.text, 'html.parser')

    tbody = r_suop.find('tbody')
    tbody_rows = tbody.find_all('tr')

    country = []
    country_id = []
    country_code = []
    l_id = []
    id_step = 0
    for tbody_row in tbody_rows:
        row = tbody_row.find_all('td')
        if 'universal' not in row[1].get_text():
            country.append(row[0].get_text())
            country_code.append(row[2].get_text())
            country_id.append(row[3].get_text())
            l_id.append(id_step)
            print(f'#{id_step} {row[0].get_text()}')
            id_step += 1

    while True:
        try:
            print('\nWhere are tou from? Choose a country by number.\n')
            q_id = int(input('#: '))
            if q_id < len(l_id):
                find_index = l_id.index(q_id)
                print(f'{country[find_index]}')
                step1_country_code = country_code[find_index]
                break
            else:
                print('Choose a number from the list.')
        except:
            print("That wasn't a number.")

    while True:
        try:

            print('\nNow choose another country\n')
            q_id = int(input('#: '))
            if q_id < len(l_id):
                find_index = l_id.index(q_id)
                print(f'{country[find_index]}')
                step2_country_code = country_code[find_index]
                break
            else:
                print('Choose a number from the list.')
        except:
            print("That wasn't a number.")

    while True:
        try:
            print(
                f'\nHow many {step1_country_code} do you want to convert to {step2_country_code}?')
            money = int(input('#: '))
            break
        except:
            print("That wasn't a number.")

    money_url = f'https://wise.com/gb/currency-converter/{step1_country_code}-to-{step2_country_code}-rate?amount={money}'
    money_r = requests.get(money_url)
    money_suop = BeautifulSoup(money_r.text, 'html.parser')

    money_rst = money_suop.find('span', 'text-success')
    exchanged_money = float(money_rst.get_text()) * money


if __name__ == '__main__':
    main()
