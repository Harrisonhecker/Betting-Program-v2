import requests
import time
from bs4 import BeautifulSoup



# The Matchup class simulates a matchup between two basketball teams and provides functions for accessing related data
class Matchup:

    __team_one_points_column = None
    __team_two_points_column = None
    __team_one_url = None
    __team_two_url = None
    __team_one_soup = None
    __team_two_soup = None

    # Inputs
    #   @param "team_one" - string
    #       a url specifying the link to the first team in the matchup
    #   @param "team_two" - string
    #       a url specifying the link to the second team in the matchup
    # Outputs
    #   None
    # Purpose
    #   Initialize the matchup     
    def __init__(self, team_one, team_two):
        self.__team_one_url = team_one
        self.__team_two_url = team_two

        self.init_soups()
        self.find_points_column()
    
    # Inputs
    #   @param "self" 
    #       the variable that references the class itself
    # Outputs
    #   None
    # Purpose
    #   Webscrape the schedules for the two teams and instantiate parsers for each webpage
    def init_soups(self):
        response_one = requests.get(self.__team_one_url)
        self.__team_one_soup = BeautifulSoup(response_one.text, 'html.parser')

        response_two = requests.get(self.__team_two_url)
        self.__team_two_soup = BeautifulSoup(response_two.text, 'html.parser')

    # Inputs
    #   @param "self" 
    #       the variable that references the class itself
    # Outputs
    #   None
    # Purpose
    #   Save the column that specifies the points each team scored per game
    def find_points_column(self):
        table_one = self.__team_one_soup.find('table', {'id': 'schedule'})
        self.__team_one_points_column = table_one.find_all('td', {'data-stat': 'pts'})

        table_two = self.__team_two_soup.find('table', {'id': 'schedule'})
        self.__team_two_points_column = table_two.find_all('td', {'data-stat': 'pts'})

        
    def compute_average(self):
        total_one = 0
        total_two = 0
        counter_one = 0
        counter_two = 0

        for score in self.__team_one_points_column:
            if score.text == '' or int(score.text) == 0:
                pass
            else:
                total_one += int(score.text)
                counter_one += 1

        for score in self.__team_two_points_column:
            if score.text == '' or int(score.text) == 0:
                pass
            else:
                total_two += int(score.text)
                counter_two += 1

        average_one = total_one / counter_one
        average_two = total_two / counter_two
        return average_one, average_two
        


