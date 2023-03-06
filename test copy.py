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

if osu() > michigan():
    print(f"osu is better ({osu()}>{round(michigan(),2)}")
elif osu() < michigan():
    print(f"michigan is better ({round(michigan(),2)} > {osu()})")
else:
    print("tie")
