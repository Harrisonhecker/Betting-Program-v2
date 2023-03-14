import requests
import time
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


# Inputs
#   None
# Outputs
#    None
# Purpose
#    This method queries the school index of www.sports-reference.com. It finds the table that lists all of the schools, finds each of the "td" elements with the schools, and then pulls the links from these elements. Then, for each link, it constructs the URL for the school's schedule page and then calls "find_average()" to compute the teams average points for the season.

def all_teams():
    
    # Query the school index and create an html parser
    url='https://www.sports-reference.com/cbb/schools/'
    response = requests.get(url)
    #print("response code: " + str(response))
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the school table and pull out the links
    table = soup.find('table', {'id': 'NCAAM_schools'})
    body = table.find_all('td', {'data-stat': 'school_name'})
    links = table.find_all('a')

    # Iterate over the links to construct the schedule page and then call "find_average()"
    for i, element in enumerate(links):
        pre_link_string = str(element.get('href'))
        post_link_string = 'https://www.sports-reference.com' + pre_link_string + '2023-schedule.html'
        name = body[i].text

        find_average(post_link_string, name)

        print("\nSleeping\n")
        time.sleep(2.0)


#
# Inputs
#   @param "url" - string
#       a url corresponding to a school's schedule page on www.sports-reference.com
#   @param "name" - string
#       the name of the school
# Outputs
#   None
# Purpose
#   This method takes a "url" parameter that contains the url for a school's schedule page on www.sports-reference.com. It also takes a "name" parameter that is the name of the #  school. It then queries the webpage, finds the schedule table, and then finds the column that contains the points the team scored for the game. It then iterates over the column to calculate the average points per game and prints that out to the console.
def find_average(url, name):
    
    # Query the webpage
    response = requests.get(url)

    # If query was successful, proceed with printing
    if response.status_code == 200:
        
        # Create an html parser
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find column with points scored each game
        table = soup.find('table', {'id': 'schedule'})
        body = table.find_all('td', {'data-stat': 'pts'})

        # Calculate and print out average points per game 
        total_points = 0
        total_games = 0
        average = 0
        for item in body:
            if item.text == '' or int(item.text) == 0:
                pass
            else:
                total_points += int(item.text)
                total_games += 1

        average = total_points / total_games
        print("Average Points Per Game For " + str(name) + ": " + str(average))
        
        return
    
    # If query was not successful, print out error message
    else:
        print(name + ' does not have 2022-2023 season.')
        return






#print(all_teams())
response = requests.get('https://www.sports-reference.com/cbb/schools/ohio-state/men/2023-gamelogs.html')
soup = BeautifulSoup(response.text, 'html.parser')
basicTable = soup.find('table', {'id': 'sgl-basic_NCAAM'})
#print(basicTable)
#for i, item in enumerate(basicTable):
for i, item in enumerate(basicTable.contents[7].contents):
    if (str(item).__contains__('pts') and not str(item).__contains__('aria-label')):
        print("Child " + str(i) + ":")
        print(item)
        print()

