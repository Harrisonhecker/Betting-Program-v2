from matchup import *
from team import *



'''match = Matchup("https://www.sports-reference.com/cbb/schools/ohio-state/men/2023-schedule.html", "https://www.sports-reference.com/cbb/schools/michigan/men/2023-schedule.html")

average1, average2 = match.compute_average()

print("Ohio State averages " + str(average1) + " points per game")
print("TTUN averages " + str(average2) + " points per game")'''

'''osu = Team('ohio-state', 109.2, 103.9)
print("OSU Expected Points: " + str(osu.predicted_points))
print("OSU Coefficient of Determination: " + str(osu.coefficient_of_determination))'''

'''boise = Team('boise-state', 104.1, 92.8)
boise.start()
print("Boise Expected Points: " + str(boise.predicted_points))


memphis = Team('memphis', 105.8, 96.2)
memphis.start()
print("Memphis Expected Points: " + str(memphis.predicted_points))'''

kansas = Team('texas')
howard = Team('colgate')

kansas.predict_score(howard.current_sos, howard.current_srs, howard.avg_FGs, howard.avg_FG_attempts, howard.avg_FG_percent, howard.avg_3Ps, howard.avg_3P_attempts, howard.avg_3P_percent, howard.avg_FTs, howard.avg_FT_attempts, howard.avg_FT_percent, howard.avg_off_rebounds, howard.avg_def_rebounds, howard.avg_total_rebounds, howard.avg_rebound_diff, howard.avg_assists, howard.avg_steals, howard.avg_blocks, howard.avg_turnovers, howard.avg_PFs)

howard.predict_score(kansas.current_sos, kansas.current_srs, kansas.avg_FGs, kansas.avg_FG_attempts, kansas.avg_FG_percent, kansas.avg_3Ps, kansas.avg_3P_attempts, kansas.avg_3P_percent, kansas.avg_FTs, kansas.avg_FT_attempts, kansas.avg_FT_percent, kansas.avg_off_rebounds, kansas.avg_def_rebounds, kansas.avg_total_rebounds, kansas.avg_rebound_diff, kansas.avg_assists, kansas.avg_steals, kansas.avg_blocks, kansas.avg_turnovers, kansas.avg_PFs)

print("Kansas Expected Points: " + str(kansas.predicted_points))
print("Kansas Coefficient of Determination: " + str(kansas.coefficient_of_determination))
print()
print("Howard Expected Points: " + str(howard.predicted_points))
print("Howard Coefficient of Determination: " + str(howard.coefficient_of_determination))

'''texas = Team('texas', 109.5, 94.8)
colgate = Team('colgate', 115.1, 101.0)
print("Texas Expected Points: " + str(texas.predicted_points))
print("Colgate Expected Points: " + str(colgate.predicted_points))
print("Texas Average Points: " + str(texas.avg_points))
print("Colgate Average Points: " + str(colgate.avg_points))'''