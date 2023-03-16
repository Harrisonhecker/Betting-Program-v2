import requests
import time
from bs4 import BeautifulSoup

import numpy as np
from sklearn.linear_model import LinearRegression
from team import *

kansas = Team('kansas')
howard = Team('howard')


print(kansas.avg_points)






'''
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
            #sos_one = float(x.text[5:9])
            start = x.text.index(':')
            end = x.text.index('(')
            sos_one = x.text[start+2:end]
            print(sos_one)
            print(float(sos_one))
        if x.text[0:3] == 'SRS':
            start = x.text.index(':')
            end = x.text.index('(')
            sos_two = x.text[start+2:end]
            print(sos_two)
            print(float(sos_two))
        if x.text[0:4] == 'ORtg':
            start = x.text.index(':')
            end = x.text.index('(')
            sos_three = x.text[start+2:end]
            print(sos_three)
            print(float(sos_three))
        if x.text[0:4] == 'DRtg':
            start = x.text.index(':')
            end = x.text.index('(')
            sos_four = x.text[start+2:end]
            print(sos_four)
            print(float(sos_four))
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



def main():
    list_teams('https://www.sports-reference.com/cbb/seasons/men/2023.html')

    team_one_data = team_one_sos('maryland')
    team_two_data = team_two_sos('west-virginia')
    print(f"Maryland SOS: {team_one_data}")
    print(f"West Virginia SOS: {team_two_data}")






from team import *
from global_variables import *
from matchup import *
#MULTIPLE LINEAR REGRESSION

kansas = Team('kansas', 50, 50)
howard = Team('howard', 50, 50)

kansas_points = kansas.avg_points
time.sleep(2)
kansas_sos = team_one_sos('kansas')
time.sleep(2)
howard_points = howard.avg_points
time.sleep(2)
howard_sos = team_two_sos('howard')

kansas_value = kansas_points * kansas_sos
howard_value = howard_points * howard_sos

print(kansas_value)
print(howard_value)
if kansas_value > howard_value:
    print('Kansas wins')
else:
    print('Howard wins')



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


team_one_sos('kansas')


def __main__():
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

    

'''