import requests


def main(location):
    url = f'https://wttr.in/{location}?nTqM&lang=ru'
    response = requests.get(url)
    response.raise_for_status()
    print(response.text)


if __name__ == "__main__":
    locations = ['Лондон', 'Шереметьево', 'Череповец']
    for location in locations:
        main(location)
