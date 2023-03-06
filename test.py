import requests
from bs4 import BeautifulSoup
'''
url='https://www.sports-reference.com/cbb/players/zion-williamson-1.html'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
element = soup.find('td', {'data-stat': 'pts_per_g'})
print(element.text)
'''
url = 'https://www.sports-reference.com/cbb/schools/ohio-state/men/2023.html'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find('table', {'id': 'per_game'})
body = table.find_all('td', {'data-stat': 'pts_per_g'})
for item in body:
    print(item.text)