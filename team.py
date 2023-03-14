import requests
from bs4 import BeautifulSoup
from global_variables import *
import numpy as np
from sklearn.linear_model import LinearRegression

class Team:

    # Constructor
    def __init__(self, team_name, off_rating, def_rating):
        
        # Basic Table Stats (Home)
        self.__points_column = []
        self.__FGs_column = []
        self.__FG_attempts_column = []
        self.__FG_percent_column = []
        self.__3Ps_column = []
        self.__3P_attempts_column = []
        self.__3P_percent_column = []
        self.__FTs_column = []
        self.__FT_attempts_column = []
        self.__FT_percent_column = []
        self.__off_rebounds_column = []
        self.__total_rebounds_column = []
        self.__assists_column = []
        self.__steals_column = []
        self.__blocks_column = []
        self.__turnovers_column = []
        self.__PFs_column = []
        

        # Basic Table Stats (Opponent)
        self.__opp_points_column = []
        self.__opp_FGs_column = []
        self.__opp_FG_attempts_column = []
        self.__opp_FG_percent_column = []
        self.__opp_3Ps_column = []
        self.__opp_3P_attempts_column = []
        self.__opp_3P_percent_column = []
        self.__opp_FTs_column = []
        self.__opp_FT_attempts_column = []
        self.__opp_FT_percent_column = []
        self.__opp_off_rebounds_column = []
        self.__opp_total_rebounds_column = []
        self.__opp_assists_column = []
        self.__opp_steals_column = []
        self.__opp_blocks_column = []
        self.__opp_turnovers_column = []
        self.__opp_PFs_column = []

        # Advanced Table Stats
        self.__off_rating_column = []
        self.__def_rating_column = []
        self.__pace_column = []
        self.__FT_attempt_rate_column = []
        self.__3P_attempt_rate_column = []
        self.__true_shooting_percent_column = []
        self.__total_rebound_percent_column = []
        self.__assist_percent_column = []
        self.__steal_percent_column = []
        self.__block_percent_column = []
        self.__off_efg_percent_column = []
        self.__off_tov_percent_column = []
        self.__off_orb_percent_column = []
        self.__off_ft_per_fga_column = []
        self.__opp_efg_percent_column = []
        self.__opp_tov_percent_column = []
        self.__opp_drb_percent_column = []
        self.__opp_ft_per_fga_column = []

        
        # Other Stats
        self.__rebound_diff_column = []
        self.__def_rebounds_column = []
        self.__opp_rebound_diff_column = []
        self.__opp_def_rebounds_column = []
        
        
        self.__current_off_rating = None
        self.__current_def_rating = None

        # Average stats
        self.avg_points = None
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
        self.__avg_total_rebounds = None
        self.__avg_steals = None
        self.__avg_blocks = None
        self.__avg_turnovers = None
        self.__avg_PFs = None

        self.opp_avg_points = None
        self.__opp_avg_FGs = None
        self.__opp_avg_FG_attempts = None
        self.__opp_avg_FG_percent = None
        self.__opp_avg_3Ps = None
        self.__opp_avg_3P_attempts = None
        self.__opp_avg_3P_percent = None
        self.__opp_avg_FTs = None
        self.__opp_avg_FT_attempts = None
        self.__opp_avg_FT_percent = None
        self.__opp_avg_off_rebounds = None
        self.__opp_avg_total_rebounds = None
        self.__opp_avg_steals = None
        self.__opp_avg_blocks = None
        self.__opp_avg_turnovers = None
        self.__opp_avg_PFs = None

        self.__avg_off_rating = None
        self.__avg_def_rating = None
        self.__avg_pace = None
        self.__avg_ft_attempt_rate = None
        self.__avg_three_point_attempt_rate = None
        self.__avg_true_shooting_percent = None
        self.__avg_total_rebound_percent = None
        self.__avg_assist_percent = None
        self.__avg_steal_percent = None
        self.__avg_block_percent = None
        self.__avg_off_efg_percent = None
        self.__avg_off_tov_percent = None
        self.__avg_off_orb_percent = None
        self.__avg_off_ft_per_fga_percent = None
        self.__avg_def_efg_percent = None
        self.__avg_def_tov_percent = None
        self.__avg_def_drb_percent = None
        self.__avg_def_ft_per_fga_percent = None
        
        self.__avg_rebound_diff = None
        self.__avg_def_rebounds = None
        self.__opp_avg_rebound_diff = None
        self.__opp_avg_def_rebounds = None

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
                
                # Basic table stats (home)
                if (str(item).__contains__(POINTS_ID) and is_basic_table_flag):
                    self.__points_column.append(float(item.text))               
                if (str(item).__contains__(FGS_ID)):
                    self.__FGs_column.append(float(item.text))
                if (str(item).__contains__(FG_ATTEMPTS_ID)):
                    self.__FG_attempts_column.append(float(item.text))
                if (str(item).__contains__(FG_PERCENT_ID)):
                    self.__FG_percent_column.append(float(item.text))             
                if (str(item).__contains__(THREE_POINT_ID)):
                    self.__3Ps_column.append(float(item.text))
                if (str(item).__contains__(THREE_POINT_ATTEMPTS_ID)):
                    self.__3P_attempts_column.append(float(item.text))
                if (str(item).__contains__(THREE_POINT_PERCENT_ID)):
                    self.__3P_percent_column.append(float(item.text))             
                if (str(item).__contains__(FT_ID)):
                    self.__FTs_column.append(float(item.text))
                if (str(item).__contains__(FT_ATTEMPT_ID)):
                    self.__FT_attempts_column.append(float(item.text))
                if (str(item).__contains__(FT_PERCENT_ID)):
                    self.__FT_percent_column.append(float(item.text)) 
                if (str(item).__contains__(OFF_REBOUNDS_ID)):
                    self.__off_rebounds_column.append(float(item.text))
                if (str(item).__contains__(TOTAL_REBOUNDS_ID)):
                    self.__total_rebounds_column.append(float(item.text))
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

                
                # Basic table stats (opponent)
                if (str(item).__contains__(OPP_POINTS_ID) and is_basic_table_flag):
                    self.__opp_points_column.append(float(item.text))               
                if (str(item).__contains__(OPP_FGS_ID)):
                    self.__opp_FGs_column.append(float(item.text))
                if (str(item).__contains__(OPP_FG_ATTEMPTS_ID)):
                    self.__opp_FG_attempts_column.append(float(item.text))
                if (str(item).__contains__(OPP_FG_PERCENT_ID)):
                    self.__opp_FG_percent_column.append(float(item.text))             
                if (str(item).__contains__(OPP_THREE_POINT_ID)):
                    self.__opp_3Ps_column.append(float(item.text))
                if (str(item).__contains__(OPP_THREE_POINT_ATTEMPTS_ID)):
                    self.__opp_3P_attempts_column.append(float(item.text))
                if (str(item).__contains__(OPP_THREE_POINT_PERCENT_ID)):
                    self.__opp_3P_percent_column.append(float(item.text))             
                if (str(item).__contains__(OPP_FT_ID)):
                    self.__opp_FTs_column.append(float(item.text))
                if (str(item).__contains__(OPP_FT_ATTEMPT_ID)):
                    self.__opp_FT_attempts_column.append(float(item.text))
                if (str(item).__contains__(OPP_FT_PERCENT_ID)):
                    self.__opp_FT_percent_column.append(float(item.text)) 
                if (str(item).__contains__(OPP_OFF_REBOUNDS_ID)):
                    self.__opp_off_rebounds_column.append(float(item.text))
                if (str(item).__contains__(OPP_TOTAL_REBOUNDS_ID)):
                    self.__opp_total_rebounds_column.append(float(item.text))
                if (str(item).__contains__(OPP_ASSISTS_ID)):
                    self.__opp_assists_column.append(float(item.text))
                if (str(item).__contains__(OPP_STEALS_ID)):
                    self.__opp_steals_column.append(float(item.text))
                if (str(item).__contains__(OPP_BLOCKS_ID)):
                    self.__opp_blocks_column.append(float(item.text))
                if (str(item).__contains__(OPP_TURNOVERS_ID)):
                    self.__opp_turnovers_column.append(float(item.text))
                if (str(item).__contains__(OPP_PERSONAL_FOULS_ID)):
                    self.__opp_PFs_column.append(float(item.text))

                # Advanced table stats
                if (str(item).__contains__(OFF_RATING_ID) ):
                    self.__off_rating_column.append(float(item.text))
                if (str(item).__contains__(DEF_RATING_ID)):
                    self.__def_rating_column.append(float(item.text))
                if (str(item).__contains__(PACE_ID)):
                    self.__pace_column.append(float(item.text))
                if (str(item).__contains__(FT_ATTEMPT_RATE_ID)):
                    self.__FT_attempt_rate_column.append(float(item.text))
                if (str(item).__contains__(THREE_POINT_ATTEMPT_RATE_ID)):
                    self.__3P_attempt_rate_column.append(float(item.text))
                if (str(item).__contains__(TRUE_SHOOTING_PERCENT_ID)):
                    self.__true_shooting_percent_column.append(float(item.text))
                if (str(item).__contains__(TOTAL_REBOUND_PERCENT_ID)):
                    self.__total_rebound_percent_column.append(float(item.text))
                if (str(item).__contains__(ASSIST_PERCENT_ID)):
                    self.__assist_percent_column.append(float(item.text))
                if (str(item).__contains__(STEAL_PERCENT_ID)):
                    self.__steal_percent_column.append(float(item.text))
                if (str(item).__contains__(BLOCK_PERCENT_ID)):
                    self.__block_percent_column.append(float(item.text))
                if (str(item).__contains__(OFF_EFG_PERCENT_ID)):
                    self.__off_efg_percent_column.append(float(item.text))
                if (str(item).__contains__(OFF_TOV_PERCENT_ID)):
                    self.__off_tov_percent_column.append(float(item.text))
                if (str(item).__contains__(OFF_ORB_PERCENT_ID)):
                    self.__off_orb_percent_column.append(float(item.text))
                if (str(item).__contains__(OFF_FT_PER_FGA_ID)):
                    self.__off_ft_per_fga_column.append(float(item.text))
                if (str(item).__contains__(OPP_EFG_PERCENT_ID)):
                    self.__opp_efg_percent_column.append(float(item.text))
                if (str(item).__contains__(OPP_TOV_PERCENT_ID)):
                    self.__opp_tov_percent_column.append(float(item.text))
                if (str(item).__contains__(OPP_DRB_PERCENT_ID)):
                    self.__opp_drb_percent_column.append(float(item.text))
                if (str(item).__contains__(OPP_FT_PER_FGA_ID)):
                    self.__opp_ft_per_fga_column.append(float(item.text))

    def __compute_averages(self):
        
        # Basic table stats (home)
        self.avg_points = np.mean(self.__points_column)
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

        # Basic table stats (opponent)
        self.opp_avg_points = np.mean(self.__opp_points_column)
        self.__opp_avg_FGs = np.mean(self.__opp_FGs_column)
        self.__opp_avg_FG_attempts = np.mean(self.__opp_FG_attempts_column)
        self.__opp_avg_FG_percent = np.mean(self.__opp_FG_percent_column)
        self.__opp_avg_3Ps = np.mean(self.__opp_3Ps_column)
        self.__opp_avg_3P_attempts = np.mean(self.__opp_3P_attempts_column)
        self.__opp_avg_3P_percent = np.mean(self.__opp_3P_percent_column)
        self.__opp_avg_FTs = np.mean(self.__opp_FTs_column)
        self.__opp_avg_FT_attempts = np.mean(self.__opp_FT_attempts_column)
        self.__opp_avg_FT_percent = np.mean(self.__opp_FT_percent_column)
        self.__opp_avg_off_rebounds = np.mean(self.__opp_off_rebounds_column)
        self.__opp_avg_def_rebounds = np.mean(self.__opp_def_rebounds_column)
        self.__opp_avg_total_rebounds = np.mean(self.__opp_total_rebounds_column)
        self.__opp_avg_steals = np.mean(self.__opp_steals_column)
        self.__opp_avg_blocks = np.mean(self.__opp_blocks_column)
        self.__opp_avg_turnovers = np.mean(self.__opp_turnovers_column)
        self.__opp_avg_PFs = np.mean(self.__opp_PFs_column)

        # Advanced table stats 
        self.__avg_off_rating = np.mean(self.__off_rating_column)
        self.__avg_def_rating = np.mean(self.__def_rating_column)
        self.__avg_pace = np.mean(self.__pace_column)
        self.__avg_ft_attempt_rate = np.mean(self.__FT_attempt_rate_column)
        self.__avg_three_point_attempt_rate = np.mean(self.__3P_attempt_rate_column)
        self.__avg_true_shooting_percent = np.mean(self.__true_shooting_percent_column)
        self.__avg_total_rebound_percent = np.mean(self.__total_rebound_percent_column)
        self.__avg_assist_percent = np.mean(self.__assist_percent_column)
        self.__avg_steal_percent = np.mean(self.__steal_percent_column)
        self.__avg_block_percent = np.mean(self.__block_percent_column)
        self.__avg_off_efg_percent = np.mean(self.__off_efg_percent_column)
        self.__avg_off_tov_percent = np.mean(self.__off_tov_percent_column)
        self.__avg_off_orb_percent = np.mean(self.__off_orb_percent_column)
        self.__avg_off_ft_per_fga_percent = np.mean(self.__off_ft_per_fga_column)
        self.__avg_def_efg_percent = np.mean(self.__opp_efg_percent_column)
        self.__avg_def_tov_percent = np.mean(self.__opp_tov_percent_column)
        self.__avg_def_drb_percent = np.mean(self.__opp_drb_percent_column)
        self.__avg_def_ft_per_fga_percent = np.mean(self.__opp_ft_per_fga_column)

        self.__avg_rebound_diff = np.mean(self.__rebound_diff_column)
        self.__opp_avg_rebound_diff = np.mean(self.__opp_rebound_diff_column)
        self.__avg_def_rebounds = np.mean(self.__def_rebounds_column)
        self.__opp_avg_def_rebounds = np.mean(self.__opp_avg_def_rebounds)

    def __populate_rebounds(self):
        for i, item in enumerate(self.__total_rebounds_column):

            self.__rebound_diff_column.append(item - self.__opp_total_rebounds_column[i])
            self.__def_rebounds_column.append(item - self.__off_rebounds_column[i])
            self.__opp_rebound_diff_column.append(self.__opp_total_rebounds_column[i] - item)
            self.__opp_def_rebounds_column.append(self.__opp_total_rebounds_column[i] - self.__opp_off_rebounds_column[i])
        
    def __init_regression_model(self):

        '''# Create input training matrix
        print(str(self.__off_rating_column.__len__()))
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


