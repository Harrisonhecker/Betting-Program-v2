from matchup import Matchup


match = Matchup("https://www.sports-reference.com/cbb/schools/ohio-state/men/2023-schedule.html", "https://www.sports-reference.com/cbb/schools/michigan/men/2023-schedule.html")

average1, average2 = match.compute_average()

print("Ohio State averages " + str(average1) + " points per game")
print("TTUN averages " + str(average2) + " points per game")

