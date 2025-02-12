import requests


def main():
    locations = ['Лондон', 'Шереметьево', 'Череповец']
    payload = {'n': '', 'T': '', 'q': '', 'M': '', 'lang': 'ru'}
    for location in locations:
        url = f'https://wttr.in/{location}'
        response = requests.get(url, params=payload)
        response.raise_for_status()
        print(response.text)


if __name__ == '__main__':
    main()
