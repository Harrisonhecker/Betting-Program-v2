YEAR = '2023'

PRE_LINK_STRING = 'https://www.sports-reference.com/cbb/schools/'
BASIC_GAME_LOG_POST_STRING = '/men/'+ YEAR + '-gamelogs.html'
ADVANCED_GAME_LOG_POST_STRING = '/men/'+ YEAR + '-gamelogs-advanced.html'
SCHEDULE_POST_STRING = '/men/' + YEAR + '-schedule.html'

ADVANCED_TABLE_ID = 'sgl-advanced'
BASIC_TABLE_ID = 'sgl-basic_M'
SCHEDULE_TABLE_ID = 'schedule'


# Basic Table Stats (Home)
POINTS_ID = 'data-stat="pts"'
FGS_ID = 'data-stat="fg"'
FG_ATTEMPTS_ID = 'data-stat="fga"'
FG_PERCENT_ID = 'data-stat="fg_pct"'
THREE_POINT_ID = 'data-stat="fg3"'
THREE_POINT_ATTEMPTS_ID = 'data-stat="fg3a"'
THREE_POINT_PERCENT_ID = 'data-stat="fg3_pct"'
FT_ID = 'data-stat="ft"'
FT_ATTEMPT_ID = 'data-stat="fta"'
FT_PERCENT_ID = 'data-stat="ft_pct"'
OFF_REBOUNDS_ID = 'data-stat="orb"'
TOTAL_REBOUNDS_ID = 'data-stat="trb"'
ASSISTS_ID = 'data-stat="ast"'
STEALS_ID = 'data-stat="stl"'
BLOCKS_ID = 'data-stat="blk"'
TURNOVERS_ID = 'data-stat="tov"'
PERSONAL_FOULS_ID = 'data-stat="pf"'

# Basic Table Stats (Opponent)
OPP_POINTS_ID = 'data-stat="opp_pts"'
OPP_FGS_ID = 'data-stat="opp_fg"'
OPP_FG_ATTEMPTS_ID = 'data-stat="opp_fga"'
OPP_FG_PERCENT_ID = 'data-stat="opp_fg_pct"'
OPP_THREE_POINT_ID = 'data-stat="opp_fg3"'
OPP_THREE_POINT_ATTEMPTS_ID = 'data-stat="opp_fg3a"'
OPP_THREE_POINT_PERCENT_ID = 'data-stat="opp_fg3_pct"'
OPP_FT_ID = 'data-stat="opp_ft"'
OPP_FT_ATTEMPT_ID = 'data-stat="opp_fta"'
OPP_FT_PERCENT_ID = 'data-stat="opp_ft_pct"'
OPP_OFF_REBOUNDS_ID = 'data-stat="opp_orb"'
OPP_TOTAL_REBOUNDS_ID = 'data-stat="opp_trb"'
OPP_ASSISTS_ID = 'data-stat="opp_ast"'
OPP_STEALS_ID = 'data-stat="opp_stl"'
OPP_BLOCKS_ID = 'data-stat="opp_blk"'
OPP_TURNOVERS_ID = 'data-stat="opp_tov"'
OPP_PERSONAL_FOULS_ID = 'data-stat="opp_pf"'
OPP_TEAM_NAME_ID = 'data-stat="opp_team_id"'

# Advanced Table Stats
OFF_RATING_ID = 'data-stat="off_rtg"'
DEF_RATING_ID = 'data-stat="def_rtg"'
PACE_ID = 'data-stat="pace"'
FT_ATTEMPT_RATE_ID = 'data-stat="fta_per_fga_pct"'
THREE_POINT_ATTEMPT_RATE_ID = 'data-stat="fg3a_per_fga_pct"'
TRUE_SHOOTING_PERCENT_ID = 'data-stat="ts_pct"'
TOTAL_REBOUND_PERCENT_ID = 'data-stat="trb_pct"'
ASSIST_PERCENT_ID = 'data-stat="ast_pct"'
STEAL_PERCENT_ID = 'data-stat="stl_pct"'
BLOCK_PERCENT_ID = 'data-stat="blk_pct"'
OFF_EFG_PERCENT_ID = 'data-stat="efg_pct"'
OFF_TOV_PERCENT_ID = 'data-stat="tov_pct"'
OFF_ORB_PERCENT_ID = 'data-stat="orb_pct"'
OFF_FT_PER_FGA_ID = 'data-stat="ft_rate"'
OPP_EFG_PERCENT_ID = 'data-stat="opp_efg_pct"'
OPP_TOV_PERCENT_ID = 'data-stat="opp_tov_pct"'
OPP_DRB_PERCENT_ID = 'data-stat="drb_pct"'
OPP_FT_PER_FGA_ID = 'data-stat="opp_ft_rate"'

# Schedule table stats
SRS_ID = 'data-stat="srs"'
SOS_HEADER = 'SOS'
SRS_HEADER = 'SRS'
OFF_RATING_HEADER = 'ORtg'
DEF_RATING_HEADER = 'DRtg'

# SOS Dictionary
SOS_DIC = {
    "Abilene Christian": 1.13,
    "Air Force": 2.67,
    "Akron": -1.28,
    "Alabama": 10.14,
    "Alabama A&M": -7.31,
    "Alabama State": -5.92,
    "Albany (NY)": -4.56,
    "Alcorn State": -5.92,
    "American": -7.8,
    "Appalachian State": -0.87,
    "Arizona": 8.69,
    "Arizona State": 8.29,
    "Arkansas": 9.56,
    "Arkansas State": -3.15,
    "Arkansas-Pine Bluff": -4.89,
    "Army": -7.75,
    "Auburn": 9.26,
    "Austin Peay": -2.45,
    "Ball State": -3.11,
    "Baylor": 11.12,
    "Bellarmine": -1.25,
    "Belmont": -1.62,
    "Bethune-Cookman": -7.49,
    "Binghamton": -5.58,
    "Boise State": 6.52,
    "Boston College": 4.74,
    "Boston University": -6.66,
    "Bowling Green State": -3.48,
    "Bradley": -0.34,
    "Brigham Young": 5.82,
    "Brown": -2.97,
    "Bryant": -4.58,
    "Bucknell": -7.02,
    "Buffalo": 0.91,
    "Butler": 8.45,
    "Cal Poly": -0.09,
    "Cal State Bakersfield": -1.04,
    "Cal State Fullerton": 0.18,
    "Cal State Northridge": -1.29,
    "California": 8.77,
    "California Baptist": -0.47,
    "Campbell": -4.89,
    "Canisius": -3.38,
    "Central Arkansas": -3.01,
    "Central Connecticut State": -9.91,
    "Central Florida": 4.99,
    "Central Michigan": -2.29,
    "Charleston Southern": -4.43,
    "Charlotte": -0.25,
    "Chattanooga": -3.2,
    "Chicago State": -3.21,
    "Cincinnati": 5.04,
    "Clemson": 4.07,
    "Cleveland State": -4.99,
    "Coastal Carolina": -1.62,
    "Colgate": -6.72,
    "College of Charleston": -4.49,
    "Colorado": 8.71,
    "Colorado State": 6.4,
    "Columbia": -2.73,
    "Connecticut": 7.39,
    "Coppin State": -3.48,
    "Cornell": -2.76,
    "Creighton": 9.46,
    "Dartmouth": -2.74,
    "Davidson": 1.68,
    "Dayton": 1.32,
    "Delaware": -3.72,
    "Delaware State": -4.98,
    "Denver": -5.45,
    "DePaul": 9,
    "Detroit Mercy": -3.47,
    "Drake": -1.25,
    "Drexel": -5.41,
    "Duke": 7.02,
    "Duquesne": 0.11,
    "East Carolina": 1.72,
    "East Tennessee State": -4.33,
    "Eastern Illinois": -6.52,
    "Eastern Kentucky": -2.05,
    "Eastern Michigan": -1.58,
    "Eastern Washington": -1.74,
    "Elon": -4.29,
    "Evansville": -1.21,
    "Fairfield": -4.49,
    "Fairleigh Dickinson": -11.75,
    "Florida": 8.55,
    "Florida A&M": -4.63,
    "Florida Atlantic": 0.65,
    "Florida Gulf Coast": -2.96,
    "Florida International": 0.12,
    "Florida State": 6.54,
    "Fordham": -2.04,
    "Fresno State": 5.7,
    "Furman": -3.92,
    "Gardner-Webb": -4.62,
    "George Mason": 0.46,
    "George Washington": -0.44,
    "Georgetown": 7.42,
    "Georgia": 5.2,
    "Georgia Southern": -1.91,
    "Georgia State": -0.84,
    "Georgia Tech": 4.95,
    "Gonzaga": 7.5,
    "Grambling": -8.09,
    "Grand Canyon": 0.98,
    "Green Bay": -2.98,
    "Hampton": -4.53,
    "Hartford": -8.23,
    "Harvard": -2.21,
    "Hawaii": -1.78,
    "High Point": -5.19,
    "Hofstra": -2.64,
    "Holy Cross": -6.5,
    "Houston": 4.76,
    "Houston Christian": -6.66,
    "Howard": -5.79,
    "Idaho": -3.5,
    "Idaho State": -2.61,
    "Illinois": 7.69,
    "Illinois State": -3.04,
    "Illinois-Chicago": -2.84,
    "Incarnate Word": -7.99,
    "Indiana": 9.07,
    "Indiana State": -3.65,
    "Iona": -3.44,
    "Iowa": 8.81,
    "Iowa State": 10.8,
    "IUPUI": -5.33,
    "Jackson State": -4.95,
    "Jacksonville": -2.49,
    "Jacksonville State": -2.43,
    "James Madison": -2.22,
    "Kansas": 12.8,
    "Kansas City": -2.81,
    "Kansas State": 9.81,
    "Kennesaw State": -2.55,
    "Kent State": -1.35,
    "Kentucky": 8.2,
    "La Salle": 0.08,
    "Lafayette": -4.72,
    "Lamar": -7.37,
    "Lehigh": -6.12,
    "Liberty": -2.27,
    "Lindenwood": -6.13,
    "Lipscomb": -3.9,
    "Little Rock": -6.76,
    "Long Beach State": -0.09,
    "Long Island University": -7.09,
    "Longwood": -6.41,
    "Louisiana": -1.07,
    "Louisiana State": 6.95,
    "Louisiana Tech": 1.68,
    "Louisiana-Monroe": -0.4,
    "Louisville": 6.5,
    "Loyola (IL)": 0.59,
    "Loyola (MD)": -6.17,
    "Loyola Marymount": 4.83,
    "Maine": -4.73,
    "Manhattan": -4.99,
    "Marist": -5.71,
    "Marquette": 7.87,
    "Marshall": -2.7,
    "Maryland": 7.91,
    "Maryland-Baltimore County": -7.06,
    "Maryland-Eastern Shore": -5.38,
    "Massachusetts": 0.41,
    "Massachusetts-Lowell": -8.67,
    "McNeese State": -5.14,
    "Memphis": 7.1,
    "Mercer": -3.9,
    "Merrimack": -9.56,
    "Miami (FL)": 5.14,
    "Miami (OH)": -2.06,
    "Michigan": 8.93,
    "Michigan State": 11.21,
    "Middle Tennessee": 1.88,
    "Milwaukee": -4.03,
    "Minnesota": 8.22,
    "Mississippi": 7.79,
    "Mississippi State": 7.22,
    "Mississippi Valley State": -4.12,
    "Missouri": 7.26,
    "Missouri State": -0.64,
    "Monmouth": -2.59,
    "Montana": -1.5,
    "Montana State": -1.66,
    "Morehead State": -5.95,
    "Morgan State": -6,
    "Mount St. Mary's": -3.9,
    "Murray State": -1.27,
    "Navy": -6.18,
    "NC State": 5.24,
    "Nebraska": 9.32,
    "Nevada": 6.79,
    "Nevada-Las Vegas": 5.73,
    "New Hampshire": -5.78,
    "New Mexico": 5.67,
    "New Mexico State": 2.71,
    "New Orleans": -7.05,
    "Niagara": -4.5,
    "Nicholls State": -5.08,
    "NJIT": -5.73,
    "Norfolk State": -6.38,
    "North Alabama": -4.09,
    "North Carolina": 7.76,
    "North Carolina A&T": -3.75,
    "North Carolina Central": -5.98,
    "North Dakota": -2.62,
    "North Dakota State": -1.58,
    "North Florida": -2.34,
    "North Texas": 1.75,
    "Northeastern": -3.96,
    "Northern Arizona": 0.03,
    "Northern Colorado": -0.21,
    "Northern Illinois": -2.3,
    "Northern Iowa": -0.71,
    "Northern Kentucky": -3.49,
    "Northwestern": 8.42,
    "Northwestern State": -6.73,
    "Notre Dame": 4.61,
    "Oakland": -2.66,
    "Ohio": -2.32,
    "Ohio State": 9.73,
    "Oklahoma": 11.82,
    "Oklahoma State": 11.12,
    "Old Dominion": -0.53,
    "Omaha": -1.41,
    "Oral Roberts": -2.96,
    "Oregon": 9.84,
    "Oregon State": 6.91,
    "Pacific": 2.54,
    "Penn State": 8.9,
    "Pennsylvania": -1.35,
    "Pepperdine": 5.2,
    "Pittsburgh": 4.54,
    "Portland": 4.57,
    "Portland State": -0.19,
    "Prairie View": -6.5,
    "Presbyterian": -5.04,
    "Princeton": -3.02,
    "Providence": 6.03,
    "Purdue": 9.07,
    "Purdue-Fort Wayne": -4.76,
    "Queens (NC)": -4.3,
    "Quinnipiac": -5.19,
    "Radford": -4.49,
    "Rhode Island": 0.62,
    "Rice": 1.1,
    "Richmond": 0.47,
    "Rider": -4.85,
    "Robert Morris": -5.39,
    "Rutgers": 7.47,
    "Sacramento State": -1.22,
    "Sacred Heart": -11.35,
    "Saint Francis (PA)": -9.81,
    "Saint Joseph's": -0.23,
    "Saint Louis": 3.1,
    "Saint Mary's (CA)": 7.11,
    "Saint Peter's": -5.3,
    "Sam Houston State": 0.74,
    "Samford": -4.21,
    "San Diego": 3.72,
    "San Diego State": 8.39,
    "San Francisco": 4.14,
    "San Jose State": 5.71,
    "Santa Clara": 5.49,
    "Seattle": 0.9,
    "Seton Hall": 8.44,
    "Siena": -4.78,
    "South Alabama": -0.37,
    "South Carolina": 6.42,
    "South Carolina State": -3.97,
    "South Carolina Upstate": -4.06,
    "South Dakota": -2.87,
    "South Dakota State": -1.61,
    "South Florida": 2.18,
    "Southeast Missouri State": -6.63,
    "Southeastern Louisiana": -6.45,
    "Southern": -6.12,
    "Southern California": 8.12,
    "Southern Illinois": -1.76,
    "SIU Edwardsville": -7.41,
    "Southern Indiana": -7.37,
    "Southern Methodist": 5.59,
    "Southern Mississippi": -1.43,
    "Southern Utah": 2.16,
    "St. Bonaventure": -0.22,
    "St. Francis (NY)": -11.73,
    "St. John's (NY)": 6.36,
    "St. Thomas": -4.27,
    "Stanford": 7.97,
    "Stephen F. Austin": -0.5,
    "Stetson": -2.5,
    "Stonehill": -9.04,
    "Stony Brook": -4.06,
    "Syracuse": 4.16,
    "Tarleton State": 2.02,
    "TCU": 8.93,
    "Temple": 5.56,
    "Tennessee": 8.14,
    "Tennessee State": -8.77,
    "Tennessee Tech": -6.22,
    "Tennessee-Martin": -7.76,
    "Texas": 10.84,
    "Texas A&M": 7.76,
    "Texas A&M-Commerce": -7.24,
    "Texas A&M-Corpus Christi": -7.72,
    "Texas Southern": -4.52,
    "Texas State": -0.59,
    "Texas Tech": 8.75,
    "Texas-Rio Grande Valley": -0.29,
    "The Citadel": -3.64,
    "Toledo": -1.93,
    "Towson": -4.72,
    "Troy": -1.14,
    "Tulane": 3.04,
    "Tulsa": 4.05,
    "UAB": 1.25,
    "UC Davis": -1.33,
    "UC Irvine": -0.66,
    "UC Riverside": 0.07,
    "UC San Diego": -0.34,
    "UC Santa Barbara": -2.19,
    "UCLA": 8.86,
    "UNC Asheville": -5.19,
    "UNC Greensboro": -2.85,
    "UNC Wilmington": -3.04,
    "UT Arlington": 2.31,
    "Utah": 6.84,
    "Utah State": 7.21,
    "Utah Tech": 1.28,
    "Utah Valley": 0.87,
    "UTEP": 1.65,
    "UTSA": 0.98,
    "Valparaiso": -2.42,
    "Vanderbilt": 8.83,
    "Vermont": -3.74,
    "Villanova": 8.6,
    "Virginia": 6.1,
    "Virginia Commonwealth": 1.62,
    "VMI": -3.46,
    "Virginia Tech": 5.11,
    "Wagner": -11.31,
    "Wake Forest": 5.42,
    "Washington": 8.33,
    "Washington State": 8.2,
    "Weber State": -0.97,
    "West Virginia": 11.25,
    "Western Carolina": -4.2,
    "Western Illinois": -4.31,
    "Western Kentucky": 0.87,
    "Western Michigan": -1.99,
    "Wichita State": 3.66,
    "William & Mary": -4.14,
    "Winthrop": -3.58,
    "Wisconsin": 9.45,
    "Wofford": -3.16,
    "Wright State": -5.7,
    "Wyoming": 6.67,
    "Xavier": 9,
    "Yale": -1.82,
    "Youngstown State": -6.23
}


