import requests
from bs4 import BeautifulSoup
url='https://www.sports-reference.com/cbb/players/zion-williamson-1.html'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
element = soup.find('td', {'data-stat': 'pts_per_g'})
print(element.text)