import requests
import time
from bs4 import BeautifulSoup

import numpy as np
from sklearn.linear_model import LinearRegression

def list_teams(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', {'id': 'current-poll'})
    body = table.find_all('td', {'data-stat': 'school_name'})

    for x in body:
        print(x.text)



def team_one_sos(team_one_name):
    url = ('https://www.sports-reference.com/cbb/schools/' + team_one_name + '/men/2023.html')
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('div', {'data-template': 'Partials/Teams/Summary'})
    body = table.find_all('p')

    for x in body:
        if x.text[0:3] == 'SOS':
            sos_one = float(x.text[5:9])
    return sos_one



def team_two_sos(team_two_name):
    url = ('https://www.sports-reference.com/cbb/schools/' + team_two_name + '/men/2023.html')
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('div', {'data-template': 'Partials/Teams/Summary'})
    body = table.find_all('p')

    for x in body:
        if x.text[0:3] == 'SOS':
            sos_two = float(x.text[5:9])
    return sos_two


'''
def main():
    list_teams('https://www.sports-reference.com/cbb/seasons/men/2023.html')

    team_one_data = team_one_sos('maryland')
    team_two_data = team_two_sos('west-virginia')
    print(f"Maryland SOS: {team_one_data}")
    print(f"West Virginia SOS: {team_two_data}")
'''



#MULTIPLE LINEAR REGRESSION


# West Virginia opponent TRB, STL, BLK
x = [
    [33, 10, 2], 
    [34, 4, 4], 
    [34, 9, 1]
]

# West Viriginia points scored
y = [89, 78, 61]

x, y = np.array(x), np.array(y)

model = LinearRegression()
model.fit(x,y)

x_new = np.array([
                  [35, 4, 8]
                  ]).reshape((-1, 3))
y_new = model.predict(x_new)
print("West Virginia Predicted Points: " + str(y_new))


def main():
    #SINGLE LINEAR REGRESSION

    #Maryland opponent SOS (Minn, North, OSU)
    x = [8.21, 8.40, 9.71]

    # Point differential
    y = []

    x, y = np.array(x), np.array(y)

    model = LinearRegression()
    model.fit(x,y)

    x_new = np.array([
                    [35, 4, 8]
                    ]).reshape((-1, 3))
    y_new = model.predict(x_new)
    print("predicted response (new): " + str(y_new) + "\n")

