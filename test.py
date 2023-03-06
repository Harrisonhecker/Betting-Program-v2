import requests
from bs4 import BeautifulSoup
'''
url='https://www.sports-reference.com/cbb/players/zion-williamson-1.html'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
element = soup.find('td', {'data-stat': 'pts_per_g'})
print(element.text)
'''

osu_total_points = 0
osu_num_players = 0
osu_average = 0

michigan_total_points = 0
michigan_total_players = 0
michigan_average = 0

url = 'https://www.sports-reference.com/cbb/schools/ohio-state/men/2023.html'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find('table', {'id': 'per_game'})
body = table.find_all('td', {'data-stat': 'pts_per_g'})
for item in body:
    osu_total_points += float(item.text)
    osu_num_players += 1
osu_average = osu_total_points / osu_num_players

url = 'https://www.sports-reference.com/cbb/schools/michigan/men/2023.html'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find('table', {'id': 'per_game'})
body = table.find_all('td', {'data-stat': 'pts_per_g'})
for item in body:
    michigan_total_points += float(item.text)
    michigan_total_players += 1
michigan_average = michigan_total_points / michigan_total_players

print("OSU Average Player Points Per Game: " + str(osu_average))
print("Michigan Average Player Points Per Game: " + str(michigan_average))
print()
print("OSU Average Points Per Game: " + str(osu_total_points))
print("Michigan Average Points Per Game: " + str(michigan_total_points))