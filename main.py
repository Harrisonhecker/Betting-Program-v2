from matchup import *
from team import *



'''match = Matchup("https://www.sports-reference.com/cbb/schools/ohio-state/men/2023-schedule.html", "https://www.sports-reference.com/cbb/schools/michigan/men/2023-schedule.html")

average1, average2 = match.compute_average()

print("Ohio State averages " + str(average1) + " points per game")
print("TTUN averages " + str(average2) + " points per game")'''

'''osu = Team('ohio-sate', 109.2, 103.9)
print("OSU Expected Points: " + str(osu.predicted_points))
print("OSU Coefficient of Determination: " + str(osu.coefficient_of_determination))'''

'''boise = Team('boise-state', 104.1, 92.8)
boise.start()
print("Boise Expected Points: " + str(boise.predicted_points))


memphis = Team('memphis', 105.8, 96.2)
memphis.start()
print("Memphis Expected Points: " + str(memphis.predicted_points))'''

'''kansas = Team('kansas', 106.2, 96.2)
howard = Team('howard', 104.9, 100.0)
print("Kansas Expected Points: " + str(kansas.predicted_points))
print("Howard Expected Points: " + str(howard.predicted_points))'''

texas = Team('texas', 109.5, 94.8)
colgate = Team('colgate', 115.1, 101.0)
print("Texas Expected Points: " + str(texas.predicted_points))
print("Colgate Expected Points: " + str(colgate.predicted_points))
print("Texas Average Points: " + str(texas.avg_points))
print("Colgate Average Points: " + str(colgate.avg_points))