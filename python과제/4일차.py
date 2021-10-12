import os
import requests


def clear():
    return os.system('cls')


def check_url():
    _urls = input(
        'Please write a URL or URLs you want to check.(separated by comma) ')
    _urls = _urls.split(',')

    for _url in _urls:
        _url = _url.strip().lower()

        if '.com' not in _url:
            print(f'{_url} is not valid URL')

        elif ('http://' not in _url) or ('https://' not in _url):
            _url = 'http://' + _url

            try:
                r = requests.get(_url)
                if r.status_code == requests.codes.ok:
                    print(f'{_url} is up!')
                else:
                    print(f'{_url} is down')

            except:
                print(f'{_url} is down')

    while True:
        _clear_check = input('Do you want to start over? y/n ')
        _clear_check = _clear_check.lower()
        if _clear_check == 'y' or _clear_check == 'n':
            return _clear_check
        else:
            print("That's not a valid answer")


while True:
    clear_check = check_url()
    if clear_check == 'y':
        clear()
    elif clear_check == 'n':
        break
