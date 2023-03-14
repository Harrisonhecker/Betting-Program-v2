import requests
from bs4 import BeautifulSoup
from global_variables import *
import numpy as np
from sklearn.linear_model import LinearRegression

class Team:
    '''
    # Stats for multiple linear regression
    __off_rating_column = []
    __def_rating_column = []
    __rebound_diff_column = []
    __3P_attempts_column = []
    __3P_percent_column = []
    __FG_attempts_column = []
    __FG_percent_column = []

    # Other Stats
    __points_column = []
    __FGs_column = []
    __3Ps_column = []
    __FTs_column = []
    __FT_attempts_column = []
    __FT_percent_column = []
    __off_rebounds_column = []
    __def_rebounds_column = []
    __total_rebounds_column = []
    __opp_total_rebounds_column = []
    __assists_column = []
    __steals_column = []
    __blocks_column = []
    __turnovers_column = []
    __PFs_column = []
    __current_off_rating = None
    __current_def_rating = None

    # Average stats
    __avg_FGs = None
    __avg_FG_attempts = None
    __avg_FG_percent = None
    __avg_3Ps = None
    __avg_3P_attempts = None
    __avg_3P_percent = None
    __avg_FTs = None
    __avg_FT_attempts = None
    __avg_FT_percent = None
    __avg_off_rebounds = None
    __avg_def_rebounds = None
    __avg_total_rebounds = None
    __avg_steals = None
    __avg_blocks = None
    __avg_turnovers = None
    __avg_PFs = None
    __avg_points = None
    __avg_rebound_diff = None

    # Links, Parsers, and Tables
    __basic_game_log_link = None
    __advanced_game_log_link = None
    __basic_parser = None
    __advanced_parser = None
    __basic_table = None
    __advanced_table = None
    __team_name = None

    # Linear Regression Model Variables
    __regression_model = None
    __input_training_matrix = None
    __output_training_array = None
    __prediction_input_array = None
    coefficient_of_determination = None

    # Big Cajuna
    predicted_points = None
    '''
    # Constructor
    def __init__(self, team_name, off_rating, def_rating):
        
        # Stats for multiple linear regression
        self.__off_rating_column = []
        self.__def_rating_column = []
        self.__rebound_diff_column = []
        self.__3P_attempts_column = []
        self.__3P_percent_column = []
        self.__FG_attempts_column = []
        self.__FG_percent_column = []

        # Other Stats
        self.__points_column = []
        self.__FGs_column = []
        self.__3Ps_column = []
        self.__FTs_column = []
        self.__FT_attempts_column = []
        self.__FT_percent_column = []
        self.__off_rebounds_column = []
        self.__def_rebounds_column = []
        self.__total_rebounds_column = []
        self.__opp_total_rebounds_column = []
        self.__assists_column = []
        self.__steals_column = []
        self.__blocks_column = []
        self.__turnovers_column = []
        self.__PFs_column = []
        self.__current_off_rating = None
        self.__current_def_rating = None

        # Average stats
        self.__avg_FGs = None
        self.__avg_FG_attempts = None
        self.__avg_FG_percent = None
        self.__avg_3Ps = None
        self.__avg_3P_attempts = None
        self.__avg_3P_percent = None
        self.__avg_FTs = None
        self.__avg_FT_attempts = None
        self.__avg_FT_percent = None
        self.__avg_off_rebounds = None
        self.__avg_def_rebounds = None
        self.__avg_total_rebounds = None
        self.__avg_steals = None
        self.__avg_blocks = None
        self.__avg_turnovers = None
        self.__avg_PFs = None
        self.avg_points = None
        self.__avg_rebound_diff = None

        # Links, Parsers, and Tables
        self.__basic_game_log_link = None
        self.__advanced_game_log_link = None
        self.__basic_parser = None
        self.__advanced_parser = None
        self.__basic_table = None
        self.__advanced_table = None
        self.__team_name = None

        # Linear Regression Model Variables
        self.__regression_model = None
        self.__input_training_matrix = None
        self.__output_training_array = None
        self.__prediction_input_array = None
        self.coefficient_of_determination = None

        # Big Cajuna
        self.predicted_points = None
        
        # Start of actual code
        self.__team_name = team_name
        self.__basic_game_log_link = PRE_LINK_STRING + team_name + BASIC_GAME_LOG_POST_STRING
        self.__advanced_game_log_link = PRE_LINK_STRING + team_name + ADVANCED_GAME_LOG_POST_STRING

        #print("first: " + self.__basic_game_log_link)

        self.__current_off_rating = off_rating
        self.__current_def_rating = def_rating

        self.__query_tables()
        self.__init_columns()
        self.__compute_averages()
        self.__init_regression_model()
        self.__predict_score()        


    # Initialize parsers and tables
    def __query_tables(self):
        #print("second: " + str(self.__basic_game_log_link))
        basic_response = requests.get(self.__basic_game_log_link)

        if (basic_response.status_code != 200):
            raise Exception("Querying basic table for " + self.__team_name + " failed. Response code was: " + str(basic_response.status_code))
        
        self.__basic_parser = BeautifulSoup(basic_response.text, 'html.parser')
        self.__basic_table = self.__basic_parser.find('table', {'id': BASIC_TABLE_ID})

        advanced_response = requests.get(self.__advanced_game_log_link)
        
        if (advanced_response.status_code != 200):
            raise Exception("Querying advanced table for " + self.__team_name + " failed. Response code was: " + str(advanced_response.status_code))
        
        self.__advanced_parser = BeautifulSoup(advanced_response.text, 'html.parser')
        self.__advanced_table = self.__advanced_parser.find('table', {'id': ADVANCED_TABLE_ID})

    def __init_columns(self):

        for i, item in enumerate(self.__basic_table.contents[7]):
            if i % 2 != 0:
                pass
            else:
                self.__extract_info(item, True)

        for i, item in enumerate(self.__advanced_table.contents[7]):
            if i % 2 != 0:
                pass
            else:
                self.__extract_info(item, False)

        self.__populate_rebounds()

    def __extract_info(self, items, is_basic_table_flag):
        for i, item in enumerate(items.contents):

            if (not str(item).__contains__('aria-label') and item.text != ''):
                if (str(item).__contains__(OFF_RATING_ID) ):
                    self.__off_rating_column.append(float(item.text))
                if (str(item).__contains__(DEF_RATING_ID)):
                    self.__def_rating_column.append(float(item.text))

                if (str(item).__contains__(TOTAL_REBOUNDS_ID)):
                    self.__total_rebounds_column.append(float(item.text))
                if (str(item).__contains__(OPP_TOTAL_REBOUNDS_ID)):
                    self.__opp_total_rebounds_column.append(float(item.text))

                if (str(item).__contains__(THREE_POINT_ID)):
                    self.__3Ps_column.append(float(item.text))
                if (str(item).__contains__(THREE_POINT_ATTEMPTS_ID)):
                    self.__3P_attempts_column.append(float(item.text))
                if (str(item).__contains__(THREE_POINT_PERCENT_ID)):
                    self.__3P_percent_column.append(float(item.text))

                if (str(item).__contains__(FGS_ID)):
                    self.__FGs_column.append(float(item.text))
                if (str(item).__contains__(FG_ATTEMPTS_ID)):
                    self.__FG_attempts_column.append(float(item.text))
                if (str(item).__contains__(FG_PERCENT_ID)):
                    self.__FG_percent_column.append(float(item.text))
                
                if (str(item).__contains__(POINTS_ID) and is_basic_table_flag):
                    self.__points_column.append(float(item.text))

                if (str(item).__contains__(FT_ID)):
                    self.__FTs_column.append(float(item.text))
                if (str(item).__contains__(FT_ATTEMPT_ID)):
                    self.__FT_attempts_column.append(float(item.text))
                if (str(item).__contains__(FT_PERCENT_ID)):
                    self.__FT_percent_column.append(float(item.text))            
                
                if (str(item).__contains__(OFF_REBOUNDS_ID)):
                    self.__off_rebounds_column.append(float(item.text))

                if (str(item).__contains__(ASSISTS_ID)):
                    self.__assists_column.append(float(item.text))

                if (str(item).__contains__(STEALS_ID)):
                    self.__steals_column.append(float(item.text))
                
                if (str(item).__contains__(BLOCKS_ID)):
                    self.__blocks_column.append(float(item.text))
                
                if (str(item).__contains__(TURNOVERS_ID)):
                    self.__turnovers_column.append(float(item.text))
                
                if (str(item).__contains__(PERSONAL_FOULS_ID)):
                    self.__PFs_column.append(float(item.text))

    def __compute_averages(self):
        self.__avg_FGs = np.mean(self.__FGs_column)
        self.__avg_FG_attempts = np.mean(self.__FG_attempts_column)
        self.__avg_FG_percent = np.mean(self.__FG_percent_column)
        self.__avg_3Ps = np.mean(self.__3Ps_column)
        self.__avg_3P_attempts = np.mean(self.__3P_attempts_column)
        self.__avg_3P_percent = np.mean(self.__3P_percent_column)
        self.__avg_FTs = np.mean(self.__FTs_column)
        self.__avg_FT_attempts = np.mean(self.__FT_attempts_column)
        self.__avg_FT_percent = np.mean(self.__FT_percent_column)
        self.__avg_off_rebounds = np.mean(self.__off_rebounds_column)
        self.__avg_def_rebounds = np.mean(self.__def_rebounds_column)
        self.__avg_total_rebounds = np.mean(self.__total_rebounds_column)
        self.__avg_steals = np.mean(self.__steals_column)
        self.__avg_blocks = np.mean(self.__blocks_column)
        self.__avg_turnovers = np.mean(self.__turnovers_column)
        self.__avg_PFs = np.mean(self.__PFs_column)
        self.avg_points = np.mean(self.__points_column)
        self.__avg_rebound_diff = np.mean(self.__rebound_diff_column)

    def __populate_rebounds(self):
        for i, item in enumerate(self.__total_rebounds_column):

            #print(self.__opp_total_rebounds_column)
            #print(self.__off_rebounds_column)
            self.__rebound_diff_column.append(item - self.__opp_total_rebounds_column[i])

            self.__def_rebounds_column.append(item - self.__off_rebounds_column[i])
        
    def __init_regression_model(self):

        # Create input training matrix
        '''print(str(self.__off_rating_column.__len__()))
        print(str(self.__def_rating_column.__len__()))
        print(str(self.__rebound_diff_column.__len__()))
        print(str(self.__3P_attempts_column.__len__()))
        print(str(self.__3P_percent_column.__len__()))
        print(str(self.__FG_attempts_column.__len__()))
        print(str(self.__FG_percent_column.__len__()))'''

        '''print(str(self.__off_rating_column))
        print(str(self.__def_rating_column))
        print(str(self.__rebound_diff_column))
        print(str(self.__3P_attempts_column))
        print(str(self.__3P_percent_column))
        print(str(self.__FG_attempts_column))
        print(str(self.__FG_percent_column))'''

        pre_transposed = np.array([self.__off_rating_column, self.__def_rating_column, self.__rebound_diff_column, self.__3P_attempts_column, self.__3P_percent_column, self.__FG_attempts_column, self.__FG_percent_column])

        self.__input_training_matrix = pre_transposed.transpose()

        # Create output training array
        self.__output_training_array = self.__points_column

        '''print(self.__input_training_matrix.__len__())
        print(self.__output_training_array.__len__())'''

        #print(self.__input_training_matrix)
        #print(self.__output_training_array)

        # Create model and fit to data
        self.__regression_model = LinearRegression()
        self.__regression_model.fit(self.__input_training_matrix, self.__output_training_array)
        self.coefficient_of_determination = self.__regression_model.score(self.__input_training_matrix, self.__output_training_array)

    def __predict_score(self):
        
        # Create input prediction array
        self.__prediction_input_array = np.array([self.__current_off_rating, self.__current_def_rating, self.__avg_rebound_diff, self.__avg_3P_attempts, self.__avg_3P_percent, self.__avg_FG_attempts, self.__avg_FG_percent]).reshape((-1, 7))

        # Predict and save score
        self.predicted_points = self.__regression_model.predict(self.__prediction_input_array)


