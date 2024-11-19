import pandas as pd

#---------------------- Activity 1 -----------------------

# df = pd.read_csv("results.csv")
# different_tournaments = df["tournament"].nunique()
# print(f"There are {different_tournaments} different tournaments within these results.")

# matches_per_tournament = df.groupby("tournament").size()
# print(matches_per_tournament)

# most_common_home_team = df["home_team"].value_counts().idxmax()
# count_most_common = df["home_team"].value_counts().max()
# print(f"The most reported home team is {most_common_home_team} with {count_most_common} appearances.")  

#---------------------- Activity 2 -----------------------

df = pd.read_csv("results.csv")

enland_home_games = df[df["home_team"] ==  "England"].shape[0]
print(f"England had {enland_home_games} home games.")

mean_home_goals = df["home_score"].mean()
england_home_games = df[df["home_team"] == "England"]
above_average_england_home_goals = england_home_games[england_home_games["home_score"] > mean_home_goals].shape[0]
print(f"England scored above the average amount of goals {above_average_england_home_goals} times.")