import requests
from bs4 import BeautifulSoup
from global_variables import *
import numpy as np
from sklearn.linear_model import LinearRegression

class Team:

    # Constructor
    def __init__(self, team_name):
        
        # Basic Table Stats (Home)
        self.points_column = []
        self.FGs_column = []
        self.FG_attempts_column = []
        self.FG_percent_column = []
        self.three_points_column = []
        self.three_point_attempts_column = []
        self.three_point_percent_column = []
        self.FTs_column = []
        self.FT_attempts_column = []
        self.FT_percent_column = []
        self.off_rebounds_column = []
        self.total_rebounds_column = []
        self.assists_column = []
        self.steals_column = []
        self.blocks_column = []
        self.turnovers_column = []
        self.PFs_column = []
        

        # Basic Table Stats (Opponent)
        self.opp_points_column = []
        self.opp_FGs_column = []
        self.opp_FG_attempts_column = []
        self.opp_FG_percent_column = []
        self.opp_3Ps_column = []
        self.opp_3P_attempts_column = []
        self.opp_3P_percent_column = []
        self.opp_FTs_column = []
        self.opp_FT_attempts_column = []
        self.opp_FT_percent_column = []
        self.opp_off_rebounds_column = []
        self.opp_total_rebounds_column = []
        self.opp_assists_column = []
        self.opp_steals_column = []
        self.opp_blocks_column = []
        self.opp_turnovers_column = []
        self.opp_PFs_column = []
        self.opp_sos_column = []

        # Advanced Table Stats
        self.off_rating_column = []
        self.def_rating_column = []
        self.pace_column = []
        self.FT_attempt_rate_column = []
        self.three_point_attempt_rate_column = []
        self.true_shooting_percent_column = []
        self.total_rebound_percent_column = []
        self.assist_percent_column = []
        self.steal_percent_column = []
        self.block_percent_column = []
        self.off_efg_percent_column = []
        self.off_tov_percent_column = []
        self.off_orb_percent_column = []
        self.off_ft_per_fga_column = []
        self.opp_efg_percent_column = []
        self.opp_tov_percent_column = []
        self.opp_drb_percent_column = []
        self.opp_ft_per_fga_column = []

        
        # Other Stats
        self.rebound_diff_column = []
        self.def_rebounds_column = []
        self.srs_column = []
        self.opp_rebound_diff_column = []
        self.opp_def_rebounds_column = []
        
        
        self.current_off_rating = None
        self.current_def_rating = None
        self.current_srs = None
        self.current_sos = None

        # Average stats
        self.avg_points = None
        self.avg_FGs = None
        self.avg_FG_attempts = None
        self.avg_FG_percent = None
        self.avg_3Ps = None
        self.avg_3P_attempts = None
        self.avg_3P_percent = None
        self.avg_FTs = None
        self.avg_FT_attempts = None
        self.avg_FT_percent = None
        self.avg_off_rebounds = None
        self.avg_total_rebounds = None
        self.avg_assists = None
        self.avg_steals = None
        self.avg_blocks = None
        self.avg_turnovers = None
        self.avg_PFs = None
        self.avg_srs = None

        self.opp_avg_points = None
        self.opp_avg_FGs = None
        self.opp_avg_FG_attempts = None
        self.opp_avg_FG_percent = None
        self.opp_avg_3Ps = None
        self.opp_avg_3P_attempts = None
        self.opp_avg_3P_percent = None
        self.opp_avg_FTs = None
        self.opp_avg_FT_attempts = None
        self.opp_avg_FT_percent = None
        self.opp_avg_off_rebounds = None
        self.opp_avg_total_rebounds = None
        self.opp_avg_assists = None
        self.opp_avg_steals = None
        self.opp_avg_blocks = None
        self.opp_avg_turnovers = None
        self.opp_avg_PFs = None

        self.avg_off_rating = None
        self.avg_def_rating = None
        self.avg_pace = None
        self.avg_ft_attempt_rate = None
        self.avg_3P_attempt_rate = None
        self.avg_true_shooting_percent = None
        self.avg_total_rebound_percent = None
        self.avg_assist_percent = None
        self.avg_steal_percent = None
        self.avg_block_percent = None
        self.avg_off_efg_percent = None
        self.avg_off_tov_percent = None
        self.avg_off_orb_percent = None
        self.avg_off_ft_per_fga_percent = None
        self.avg_def_efg_percent = None
        self.avg_def_tov_percent = None
        self.avg_def_drb_percent = None
        self.avg_def_ft_per_fga_percent = None
        
        self.avg_rebound_diff = None
        self.avg_def_rebounds = None
        self.opp_avg_rebound_diff = None
        self.opp_avg_def_rebounds = None
        self.opp_avg_sos = None

        # Links, Parsers, and Tables
        self.__basic_game_log_link = None
        self.__advanced_game_log_link = None
        self.__schedule_link = None
        self.__basic_parser = None
        self.__advanced_parser = None
        self.__schedule_parser = None
        self.__basic_table = None
        self.__advanced_table = None
        self.__schedule_table = None
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
        self.__schedule_link = PRE_LINK_STRING + team_name + SCHEDULE_POST_STRING

        self.__query_tables()
        self.__init_columns()
        self.__find_current_info()
        self.__compute_averages()

        print(self.opp_sos_column)
        self.__init_regression_model()      

    # Initialize parsers and tables
    def __query_tables(self):

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

        schedule_response = requests.get(self.__schedule_link)

        if (schedule_response.status_code != 200):
            raise Exception("Querying schedule table for " + self.__team_name + " failed. Response code was: " + str(schedule_response.status_code))
        
        self.__schedule_parser = BeautifulSoup(schedule_response.text, 'html.parser')
        self.__schedule_table = self.__schedule_parser.find('table', {'id': SCHEDULE_TABLE_ID})

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
        
        for i, item in enumerate(self.__schedule_table.contents[7]):
            if i % 2 != 0:
                pass
            else:
                self.__extract_srs(item)


        self.__populate_rebounds()

    def __extract_srs(self, items):
        
        if (items.contents[9].text == ''):
            return
        else:
            for i, item in enumerate(items.contents):

                if (not str(item).__contains__('aria-label')):

                    if (str(item).__contains__(SRS_ID)):
                        if (item.text == ''):
                            self.srs_column.append(float(0))
                        else: 
                            self.srs_column.append(float(item.text))

    def __extract_info(self, items, is_basic_table_flag):
        for i, item in enumerate(items.contents):

            if (not str(item).__contains__('aria-label') and item.text != ''):
                
                # Basic table stats (home)
                if (str(item).__contains__(POINTS_ID) and is_basic_table_flag):
                    self.points_column.append(float(item.text))               
                if (str(item).__contains__(FGS_ID)):
                    self.FGs_column.append(float(item.text))
                if (str(item).__contains__(FG_ATTEMPTS_ID)):
                    self.FG_attempts_column.append(float(item.text))
                if (str(item).__contains__(FG_PERCENT_ID)):
                    self.FG_percent_column.append(float(item.text))             
                if (str(item).__contains__(THREE_POINT_ID)):
                    self.three_points_column.append(float(item.text))
                if (str(item).__contains__(THREE_POINT_ATTEMPTS_ID)):
                    self.three_point_attempts_column.append(float(item.text))
                if (str(item).__contains__(THREE_POINT_PERCENT_ID)):
                    self.three_point_percent_column.append(float(item.text))             
                if (str(item).__contains__(FT_ID)):
                    self.FTs_column.append(float(item.text))
                if (str(item).__contains__(FT_ATTEMPT_ID)):
                    self.FT_attempts_column.append(float(item.text))
                if (str(item).__contains__(FT_PERCENT_ID)):
                    self.FT_percent_column.append(float(item.text)) 
                if (str(item).__contains__(OFF_REBOUNDS_ID)):
                    self.off_rebounds_column.append(float(item.text))
                if (str(item).__contains__(TOTAL_REBOUNDS_ID)):
                    self.total_rebounds_column.append(float(item.text))
                if (str(item).__contains__(ASSISTS_ID)):
                    self.assists_column.append(float(item.text))
                if (str(item).__contains__(STEALS_ID)):
                    self.steals_column.append(float(item.text))
                if (str(item).__contains__(BLOCKS_ID)):
                    self.blocks_column.append(float(item.text))
                if (str(item).__contains__(TURNOVERS_ID)):
                    self.turnovers_column.append(float(item.text))
                if (str(item).__contains__(PERSONAL_FOULS_ID)):
                    self.PFs_column.append(float(item.text))

                
                # Basic table stats (opponent)
                if (str(item).__contains__(OPP_POINTS_ID) and is_basic_table_flag):
                    self.opp_points_column.append(float(item.text))               
                if (str(item).__contains__(OPP_FGS_ID)):
                    self.opp_FGs_column.append(float(item.text))
                if (str(item).__contains__(OPP_FG_ATTEMPTS_ID)):
                    self.opp_FG_attempts_column.append(float(item.text))
                if (str(item).__contains__(OPP_FG_PERCENT_ID)):
                    self.opp_FG_percent_column.append(float(item.text))             
                if (str(item).__contains__(OPP_THREE_POINT_ID)):
                    self.opp_3Ps_column.append(float(item.text))
                if (str(item).__contains__(OPP_THREE_POINT_ATTEMPTS_ID)):
                    self.opp_3P_attempts_column.append(float(item.text))
                if (str(item).__contains__(OPP_THREE_POINT_PERCENT_ID)):
                    self.opp_3P_percent_column.append(float(item.text))             
                if (str(item).__contains__(OPP_FT_ID)):
                    self.opp_FTs_column.append(float(item.text))
                if (str(item).__contains__(OPP_FT_ATTEMPT_ID)):
                    self.opp_FT_attempts_column.append(float(item.text))
                if (str(item).__contains__(OPP_FT_PERCENT_ID)):
                    self.opp_FT_percent_column.append(float(item.text)) 
                if (str(item).__contains__(OPP_OFF_REBOUNDS_ID)):
                    self.opp_off_rebounds_column.append(float(item.text))
                if (str(item).__contains__(OPP_TOTAL_REBOUNDS_ID)):
                    self.opp_total_rebounds_column.append(float(item.text))
                if (str(item).__contains__(OPP_ASSISTS_ID)):
                    self.opp_assists_column.append(float(item.text))
                if (str(item).__contains__(OPP_STEALS_ID)):
                    self.opp_steals_column.append(float(item.text))
                if (str(item).__contains__(OPP_BLOCKS_ID)):
                    self.opp_blocks_column.append(float(item.text))
                if (str(item).__contains__(OPP_TURNOVERS_ID)):
                    self.opp_turnovers_column.append(float(item.text))
                if (str(item).__contains__(OPP_PERSONAL_FOULS_ID)):
                    self.opp_PFs_column.append(float(item.text))

                if (str(item).__contains__(OPP_TEAM_NAME_ID) and is_basic_table_flag):
                    sos = SOS_DIC[item.text]
                    self.opp_sos_column.append(sos)

                # Advanced table stats
                if (str(item).__contains__(OFF_RATING_ID) ):
                    self.off_rating_column.append(float(item.text))
                if (str(item).__contains__(DEF_RATING_ID)):
                    self.def_rating_column.append(float(item.text))
                if (str(item).__contains__(PACE_ID)):
                    self.pace_column.append(float(item.text))
                if (str(item).__contains__(FT_ATTEMPT_RATE_ID)):
                    self.FT_attempt_rate_column.append(float(item.text))
                if (str(item).__contains__(THREE_POINT_ATTEMPT_RATE_ID)):
                    self.three_point_attempt_rate_column.append(float(item.text))
                if (str(item).__contains__(TRUE_SHOOTING_PERCENT_ID)):
                    self.true_shooting_percent_column.append(float(item.text))
                if (str(item).__contains__(TOTAL_REBOUND_PERCENT_ID)):
                    self.total_rebound_percent_column.append(float(item.text))
                if (str(item).__contains__(ASSIST_PERCENT_ID)):
                    self.assist_percent_column.append(float(item.text))
                if (str(item).__contains__(STEAL_PERCENT_ID)):
                    self.steal_percent_column.append(float(item.text))
                if (str(item).__contains__(BLOCK_PERCENT_ID)):
                    self.block_percent_column.append(float(item.text))
                if (str(item).__contains__(OFF_EFG_PERCENT_ID)):
                    self.off_efg_percent_column.append(float(item.text))
                if (str(item).__contains__(OFF_TOV_PERCENT_ID)):
                    self.off_tov_percent_column.append(float(item.text))
                if (str(item).__contains__(OFF_ORB_PERCENT_ID)):
                    self.off_orb_percent_column.append(float(item.text))
                if (str(item).__contains__(OFF_FT_PER_FGA_ID)):
                    self.off_ft_per_fga_column.append(float(item.text))
                if (str(item).__contains__(OPP_EFG_PERCENT_ID)):
                    self.opp_efg_percent_column.append(float(item.text))
                if (str(item).__contains__(OPP_TOV_PERCENT_ID)):
                    self.opp_tov_percent_column.append(float(item.text))
                if (str(item).__contains__(OPP_DRB_PERCENT_ID)):
                    self.opp_drb_percent_column.append(float(item.text))
                if (str(item).__contains__(OPP_FT_PER_FGA_ID)):
                    self.opp_ft_per_fga_column.append(float(item.text))

    def __find_current_info(self):
        body = self.__schedule_parser.find_all('p')

        for x in body:
            if x.text[0:3] == SOS_HEADER:
                start = x.text.index(':')
                end = x.text.index('(')
                self.current_sos = float(x.text[start+2:end])
            if x.text[0:3] == SRS_HEADER:
                start = x.text.index(':')
                end = x.text.index('(')
                self.current_srs = float(x.text[start+2:end])
            if x.text[0:4] == OFF_RATING_HEADER:
                start = x.text.index(':')
                end = x.text.index('(')
                self.current_off_rating = float(x.text[start+2:end])
            if x.text[0:4] == DEF_RATING_HEADER:
                start = x.text.index(':')
                end = x.text.index('(')
                self.current_def_rating = float(x.text[start+2:end])

    def __compute_averages(self):
        
        # Basic table stats (home)
        self.avg_points = np.mean(self.points_column)
        self.avg_FGs = np.mean(self.FGs_column)
        self.avg_FG_attempts = np.mean(self.FG_attempts_column)
        self.avg_FG_percent = np.mean(self.FG_percent_column)
        self.avg_3Ps = np.mean(self.three_points_column)
        self.avg_3P_attempts = np.mean(self.three_point_attempts_column)
        self.avg_3P_percent = np.mean(self.three_point_percent_column)
        self.avg_FTs = np.mean(self.FTs_column)
        self.avg_FT_attempts = np.mean(self.FT_attempts_column)
        self.avg_FT_percent = np.mean(self.FT_percent_column)
        self.avg_off_rebounds = np.mean(self.off_rebounds_column)
        self.avg_def_rebounds = np.mean(self.def_rebounds_column)
        self.avg_total_rebounds = np.mean(self.total_rebounds_column)
        self.avg_assists = np.mean(self.assists_column)
        self.avg_steals = np.mean(self.steals_column)
        self.avg_blocks = np.mean(self.blocks_column)
        self.avg_turnovers = np.mean(self.turnovers_column)
        self.avg_PFs = np.mean(self.PFs_column)

        # Basic table stats (opponent)
        self.opp_avg_points = np.mean(self.opp_points_column)
        self.opp_avg_FGs = np.mean(self.opp_FGs_column)
        self.opp_avg_FG_attempts = np.mean(self.opp_FG_attempts_column)
        self.opp_avg_FG_percent = np.mean(self.opp_FG_percent_column)
        self.opp_avg_3Ps = np.mean(self.opp_3Ps_column)
        self.opp_avg_3P_attempts = np.mean(self.opp_3P_attempts_column)
        self.opp_avg_3P_percent = np.mean(self.opp_3P_percent_column)
        self.opp_avg_FTs = np.mean(self.opp_FTs_column)
        self.opp_avg_FT_attempts = np.mean(self.opp_FT_attempts_column)
        self.opp_avg_FT_percent = np.mean(self.opp_FT_percent_column)
        self.opp_avg_off_rebounds = np.mean(self.opp_off_rebounds_column)
        self.opp_avg_def_rebounds = np.mean(self.opp_def_rebounds_column)
        self.opp_avg_total_rebounds = np.mean(self.opp_total_rebounds_column)
        self.opp_avg_assists = np.mean(self.opp_assists_column)
        self.opp_avg_steals = np.mean(self.opp_steals_column)
        self.opp_avg_blocks = np.mean(self.opp_blocks_column)
        self.opp_avg_turnovers = np.mean(self.opp_turnovers_column)
        self.opp_avg_PFs = np.mean(self.opp_PFs_column)

        # Advanced table stats 
        self.avg_off_rating = np.mean(self.off_rating_column)
        self.avg_def_rating = np.mean(self.def_rating_column)
        self.avg_pace = np.mean(self.pace_column)
        self.avg_ft_attempt_rate = np.mean(self.FT_attempt_rate_column)
        self.avg_3P_attempt_rate = np.mean(self.three_point_attempt_rate_column)
        self.avg_true_shooting_percent = np.mean(self.true_shooting_percent_column)
        self.avg_total_rebound_percent = np.mean(self.total_rebound_percent_column)
        self.avg_assist_percent = np.mean(self.assist_percent_column)
        self.avg_steal_percent = np.mean(self.steal_percent_column)
        self.avg_block_percent = np.mean(self.block_percent_column)
        self.avg_off_efg_percent = np.mean(self.off_efg_percent_column)
        self.avg_off_tov_percent = np.mean(self.off_tov_percent_column)
        self.avg_off_orb_percent = np.mean(self.off_orb_percent_column)
        self.avg_off_ft_per_fga_percent = np.mean(self.off_ft_per_fga_column)
        self.avg_def_efg_percent = np.mean(self.opp_efg_percent_column)
        self.avg_def_tov_percent = np.mean(self.opp_tov_percent_column)
        self.avg_def_drb_percent = np.mean(self.opp_drb_percent_column)
        self.avg_def_ft_per_fga_percent = np.mean(self.opp_ft_per_fga_column)

        self.avg_rebound_diff = np.mean(self.rebound_diff_column)
        self.opp_avg_rebound_diff = np.mean(self.opp_rebound_diff_column)
        self.avg_def_rebounds = np.mean(self.def_rebounds_column)
        self.opp_avg_def_rebounds = np.mean(self.opp_avg_def_rebounds)
        self.avg_srs = np.mean(self.srs_column)
        self.opp_avg_sos = np.mean(self.opp_sos_column)

    def __populate_rebounds(self):
        for i, item in enumerate(self.total_rebounds_column):

            self.rebound_diff_column.append(item - self.opp_total_rebounds_column[i])
            self.def_rebounds_column.append(item - self.off_rebounds_column[i])
            self.opp_rebound_diff_column.append(self.opp_total_rebounds_column[i] - item)
            self.opp_def_rebounds_column.append(self.opp_total_rebounds_column[i] - self.opp_off_rebounds_column[i])
        
    def __init_regression_model(self):

        '''# Create input training matrix
        print(str(self.off_rating_column.__len__()))
        print(str(self.def_rating_column.__len__()))
        print(str(self.rebound_diff_column.__len__()))
        print(str(self.three_point_attempts_column.__len__()))
        print(str(self.three_point_percent_column.__len__()))
        print(str(self.FG_attempts_column.__len__()))
        print(str(self.FG_percent_column.__len__()))'''

        '''print(str(self.FGs_column.__len__()))
        print(str(self.srs_column.__len__()))
        print(str(self.srs_column))'''

        '''print(str(self.off_rating_column))
        print(str(self.def_rating_column))
        print(str(self.rebound_diff_column))
        print(str(self.three_point_attempts_column))
        print(str(self.three_point_percent_column))
        print(str(self.FG_attempts_column))
        print(str(self.FG_percent_column))'''

        pre_transposed = np.array([self.srs_column, self.off_rating_column, self.def_rating_column, self.rebound_diff_column, self.three_point_attempts_column, self.three_point_percent_column, self.FG_attempts_column, self.FG_percent_column])

        #pre_transposed = np.array([self.srs_column, self.FGs_column, self.FG_attempts_column, self.FG_percent_column, self.three_points_column, self.three_point_attempts_column, self.three_point_percent_column, self.FTs_column, self.FT_attempts_column, self.FT_percent_column, self.off_rebounds_column, self.def_rebounds_column, self.total_rebounds_column, self.rebound_diff_column, self.assists_column, self.steals_column, self.blocks_column, self.turnovers_column, self.PFs_column, self.opp_FGs_column, self.opp_FG_attempts_column, self.opp_FG_percent_column, self.opp_3Ps_column, self.opp_3P_attempts_column, self.opp_3P_percent_column, self.opp_FTs_column, self.opp_FT_attempts_column, self.opp_FT_percent_column, self.opp_off_rebounds_column, self.opp_def_rebounds_column, self.opp_total_rebounds_column, self.opp_rebound_diff_column, self.opp_assists_column, self.opp_steals_column, self.opp_blocks_column, self.opp_turnovers_column, self.opp_PFs_column, self.off_rating_column, self.def_rating_column, self.pace_column, self.FT_attempt_rate_column, self.three_point_attempt_rate_column, self.true_shooting_percent_column, self.total_rebound_percent_column, self.assist_percent_column, self.steal_percent_column, self.block_percent_column, self.off_efg_percent_column, self.off_tov_percent_column, self.off_orb_percent_column, self.off_ft_per_fga_column, self.opp_efg_percent_column, self.opp_tov_percent_column, self.opp_drb_percent_column, self.opp_ft_per_fga_column])

        self.__input_training_matrix = pre_transposed.transpose()

        print(self.__input_training_matrix)
        print()

        # Create output training array
        self.__output_training_array = self.points_column
        #print(self.__output_training_array)

        '''print(self.input_training_matrix.__len__())
        print(self.output_training_array.__len__())'''

        #print(self.input_training_matrix)
        #print(self.output_training_array)

        # Create model and fit to data
        self.__regression_model = LinearRegression()
        self.__regression_model.fit(self.__input_training_matrix, self.__output_training_array)
        self.coefficient_of_determination = self.__regression_model.score(self.__input_training_matrix, self.__output_training_array)

    def predict_score(self, opp_srs, opp_fgs, opp_fg_attempts, opp_fg_percent, opp_3p, opp_3p_attempts, opp_3p_percent, opp_ft, opp_ft_attempts, opp_ft_percent, opp_off_rebounds, opp_def_rebounds, opp_total_rebounds, opp_rebound_diff, opp_assists, opp_steals, opp_blocks, opp_turnovers, opp_pfs):
        
        # Create input prediction array
        self.__prediction_input_array = np.array([opp_srs, self.current_off_rating, self.current_def_rating, self.avg_rebound_diff, self.avg_3P_attempts, self.avg_3P_percent, self.avg_FG_attempts, self.avg_FG_percent]).reshape((-1, 8))
        print(self.__prediction_input_array)

        #self.__prediction_input_array = np.array([self.avg_FGs, self.avg_FG_attempts, self.avg_FG_percent, self.avg_3Ps, self.avg_3P_attempts, self.avg_3P_percent, self.avg_FTs, self.avg_FT_attempts, self.avg_FT_percent, self.avg_off_rebounds, self.avg_def_rebounds, self.avg_total_rebounds, self.avg_rebound_diff, self.avg_assists, self.avg_steals, self.avg_blocks, self.avg_turnovers, self.avg_PFs, self.opp_avg_FGs, self.opp_avg_FG_attempts, self.opp_avg_FG_percent, self.opp_avg_3Ps, self.opp_avg_3P_attempts, self.opp_avg_3P_percent, self.opp_avg_FTs, self.opp_avg_FT_attempts, self.opp_avg_FT_percent, self.opp_avg_off_rebounds, self.opp_avg_def_rebounds, self.opp_avg_total_rebounds, self.opp_avg_rebound_diff, self.opp_avg_assists, self.opp_avg_steals, self.opp_avg_blocks, self.opp_avg_turnovers, self.opp_avg_PFs, self.current_off_rating, self.current_def_rating, self.avg_pace, self.avg_ft_attempt_rate, self.avg_3P_attempt_rate, self.avg_true_shooting_percent, self.avg_total_rebound_percent, self.avg_assist_percent, self.avg_steal_percent, self.avg_block_percent, self.avg_off_efg_percent, self.avg_off_tov_percent, self.avg_off_orb_percent, self.avg_off_ft_per_fga_percent, self.avg_def_efg_percent, self.avg_def_tov_percent, self.avg_def_drb_percent, self.avg_def_ft_per_fga_percent]).reshape((-1, 54))


        #self.__prediction_input_array = np.array([opp_srs, self.avg_FGs, self.avg_FG_attempts, self.avg_FG_percent, self.avg_3Ps, self.avg_3P_attempts, self.avg_3P_percent, self.avg_FTs, self.avg_FT_attempts, self.avg_FT_percent, self.avg_off_rebounds, self.avg_def_rebounds, self.avg_total_rebounds, self.avg_rebound_diff, self.avg_assists, self.avg_steals, self.avg_blocks, self.avg_turnovers, self.avg_PFs, opp_fgs, opp_fg_attempts, opp_fg_percent, opp_3p, opp_3p_attempts, opp_3p_percent, opp_ft, opp_ft_attempts, opp_ft_percent, opp_off_rebounds, opp_def_rebounds, opp_total_rebounds, opp_rebound_diff, opp_assists, opp_steals, opp_blocks, opp_turnovers, opp_pfs, self.current_off_rating, self.current_def_rating, self.avg_pace, self.avg_ft_attempt_rate, self.avg_3P_attempt_rate, self.avg_true_shooting_percent, self.avg_total_rebound_percent, self.avg_assist_percent, self.avg_steal_percent, self.avg_block_percent, self.avg_off_efg_percent, self.avg_off_tov_percent, self.avg_off_orb_percent, self.avg_off_ft_per_fga_percent, self.avg_def_efg_percent, self.avg_def_tov_percent, self.avg_def_drb_percent, self.avg_def_ft_per_fga_percent]).reshape((-1, 55))

        # Predict and save score
        self.predicted_points = self.__regression_model.predict(self.__prediction_input_array)


