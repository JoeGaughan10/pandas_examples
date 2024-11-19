import pandas as pd

df = pd.read_excel("dev_rankings.xlsx")
#print(df)

df = df.set_index("Languages")
#print(df)

# Access specific column
#print(df[["Ranking 2019", "Ranking 2021", "Ranking 2022"]])

# Access only columns containing specified item
#print(df.loc["HTML"])

# Using slice notation
print(df.loc["Python":"HTML":1, "Python":"Ranking 2019":2])

# Using iloc[]
print(df.iloc[3])

# Using .at[] for single values
print(df.at["HTML", "Ranking 2023"])

# Using df.head()
print(df.head(2))