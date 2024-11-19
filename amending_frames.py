import pandas as pd

languages = pd.Series(["Python", "JavaScript", "HTML", "SQL"]) # pd.Series means, from the Pandas library, using Series.
position = pd.Series([3, 1, 2, 4])

df = pd.DataFrame({
    "Languages": languages,
    "Positions": position
})

#print(df.to_string(index = False))

#--------------- Apending with loc ----------------

# df.loc[4] = ["PHP", 11]
# df.loc[3.5] = ["KESL", 20]

# df = df.sort_index()
# df = df.reset_index()
# print(df)

#-------------- Apending with concat -------------

# new_data = pd.DataFrame({
#     "Languages" : ["PHP"],
#     "Positions" : [11]
# })

# df = pd.concat([df,new_data])

# print(df)

# ------------ Practise -------------

# df.loc[11] = ["PHP", 22]

# df = df.sort_index()
# df.reset_index()

# print(df)

#---------- Adding Columns --------

# df["2019 Rankings"] = [4, 1, 2, 3]

# print(df)

#--------- Adding at a specific position --------

df.insert(2, "Positions 2021", [3, 1, 2, 4])
df.insert(2, "Positions TEST", [3, 1, 2, 4])
print(df)

df = df.rename(columns={"Positions": "Positions 2023"})
print(df)

df = df.set_index("Languages")
print(df)


