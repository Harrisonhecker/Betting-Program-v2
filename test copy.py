import requests
from bs4 import BeautifulSoup

def osu():
    url='https://www.sports-reference.com/cbb/schools/ohio-state/men/2023.html#all_per_game_players'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')


    table = soup.find('table', {'id': 'per_game'})
    body = table.find_all('td', {'data-stat': 'pts_per_g'})

    total = 0
    for item in body:
        total += float(item.text)
    return total

def michigan():
    url='https://www.sports-reference.com/cbb/schools/michigan/men/2023.html#all_per_game_players'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')


    table = soup.find('table', {'id': 'per_game'})
    body = table.find_all('td', {'data-stat': 'pts_per_g'})

    total = 0
    for item in body:
        total += float(item.text)
    return total

def who_wins():
    if osu() > michigan():
        print(f"osu is better ({osu()}>{round(michigan(),2)}")
    elif osu() < michigan():
        print(f"michigan is better ({round(michigan(),2)} > {osu()})")
    else:
        print("tie")


def all_teams():
    url='https://www.sports-reference.com/cbb/schools/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    
    table = soup.find('table', {'id': 'NCAAM_schools'})
    body = table.find_all('td', {'data-stat': 'school_name'})
    links = table.find_all('a')

    for x in links:
        pre_link_string = str(x.get('href'))
        post_link_string = 'https://www.sports-reference.com' + pre_link_string + '2023-schedule.html'

        find_average(post_link_string)


def find_average(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        print(soup.title)


        table = soup.find('table', {'id': 'schedule'})
        body = table.find_all('td', {'data-stat': 'pts'})

        total = 0
        for item in body:
            if item.text == '' or int(item.text) == 0:
                pass
            else:
                print(item.text)
            #total += float(item.text)
        return
    else:
        print('team does not have 2022-2023 season')
        return






print(all_teams())

