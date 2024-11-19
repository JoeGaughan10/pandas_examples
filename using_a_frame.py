import pandas as pd

df = pd.read_csv("spotify_songs.csv")

#print(df.shape) # Displays dataframe dimensions

#print(df["playlist_genre"].value_counts()) # Displays the types of genre and their values only

# max_ms = (df["duration_ms"].max())
# min_ms = (df["duration_ms"].min())
# range_ms = max_ms - min_ms
# print(range_ms) # Prints the range in duration

#print(df.sort_values(by = ["duration_ms"])) # Sorts by duration

#print(df.groupby("playlist_genre")["duration_ms"].min()) # Gets shortest durations of each genre

mean_val = df["duration_ms"].mean()
long_tracks = df[df["duration_ms"] > mean_val]
print(long_tracks)