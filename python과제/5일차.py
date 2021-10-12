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
            q_id = int(input('#: '))

            if q_id < len(l_id):
                find_index = l_id.index(q_id)
                print(
                    f'You chose {country[find_index]}\nThe currency code is {country_code[find_index]}')
                break
            else:
                print('Choose a number from the list.')
        except:
            print("That wasn't a number.")


if __name__ == '__main__':
    main()
