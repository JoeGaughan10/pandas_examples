import pandas as pd

data_frame = pd.read_csv("results.csv")

#-------- Ways to Display Data ----------

#print(data_frame)

#data_frame.info()

# print(data_frame.describe())

#--------- Finding Percentages ------------

print(data_frame["home_score"].value_counts(normalize = True) * 100)

#--------- Specific Search ---------

mask = data_frame["home_score"] < 4

mask_df = data_frame[mask]

print(mask_df.describe())