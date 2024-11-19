import pandas as pd

#------------------- Series Examples ---------------------

# languages = pd.Series(["Python", "JavaScript", "HTML", "SQL"]) # pd.Series means, from the Pandas library, using Series.

# position = pd.Series([3, 1, 2, 4])

# print(languages)
# print(position)

#------------------- Data Frame Examples -----------------

# df = pd.DataFrame([("Anne", 30),("Bill", 27),("Charlie", 55)], columns = ["Name", "Age"])

# print(df)

#------------------ Data Frame Example 2 - Column Ttiles -----------------

# languages = pd.Series(["Python", "JavaScript", "HTML", "SQL"]) # pd.Series means, from the Pandas library, using Series.
# position = pd.Series([3, 1, 2, 4])


# # df = pd.DataFrame({
# #     "Languages": languages,
# #     "Ranking": position
# #     })

# # print(df)

# df = pd.concat([languages, position], axis = 1)
# df.columns = ["Languages", "Position"] # df.columns assigns names to the columns
# print(df)

#----------------------- Existing Structures ----------------------------

# df = pd.read_csv("speeds.csv")
# print(df)

# df = pd.read_excel("speeds.xlsx")
# print(df)

#---------------------- Creating Excel File Activity --------------------

# Data for the planets in the solar system
# data = {
#     'Name': ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'],
#     'Average Temperature (°C)': [167, 464, 14, -60, -108, -139, -197, -200],
#     'Radius (km)': [2439.7, 6051.8, 6371.0, 3389.5, 69911.0, 58232.0, 25362.0, 24622.0],
#     'Color': ['Gray', 'Yellowish-white', 'Blue and green', 'Red', 'Orange with white bands', 
#               'Yellow with brownish hues', 'Pale blue', 'Deep blue'],
#     'Interesting Feature': [
#         'Mercury has the most extreme temperature variation in the solar system.',
#         'Venus has a surface temperature that is hotter than Mercury’s, despite being farther from the Sun.',
#         'Earth is the only known planet to support life.',
#         'Mars is home to the tallest volcano in the solar system, Olympus Mons.',
#         'Jupiter is the largest planet in the solar system and has a giant storm, the Great Red Spot.',
#         'Saturn is famous for its spectacular ring system, made mostly of ice and rock.',
#         'Uranus rotates on its side, with its axis tilted over 90 degrees.',
#         'Neptune has the strongest winds in the solar system, reaching speeds of up to 2,100 km/h.'
#     ]
# }

# # Create a DataFrame
# planets_df = pd.DataFrame(data)

# file_path = "output.xlsx"

# planets_df.to_excel(file_path, index = False)

# print(f"Dataframe has been printed to {file_path}")

#----------------------- Create CSV File Test ----------------------

# data = {
#     'Name': ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'],
#     'Average Temperature (°C)': [167, 464, 14, -60, -108, -139, -197, -200],
#     'Radius (km)': [2439.7, 6051.8, 6371.0, 3389.5, 69911.0, 58232.0, 25362.0, 24622.0],
#     'Color': ['Gray', 'Yellowish-white', 'Blue and green', 'Red', 'Orange with white bands', 
#               'Yellow with brownish hues', 'Pale blue', 'Deep blue'],
#     'Interesting Feature': [
#         'Mercury has the most extreme temperature variation in the solar system.',
#         'Venus has a surface temperature that is hotter than Mercury’s, despite being farther from the Sun.',
#         'Earth is the only known planet to support life.',
#         'Mars is home to the tallest volcano in the solar system, Olympus Mons.',
#         'Jupiter is the largest planet in the solar system and has a giant storm, the Great Red Spot.',
#         'Saturn is famous for its spectacular ring system, made mostly of ice and rock.',
#         'Uranus rotates on its side, with its axis tilted over 90 degrees.',
#         'Neptune has the strongest winds in the solar system, reaching speeds of up to 2,100 km/h.'
#     ]
# }

# planets_df = pd.DataFrame(data)

# file_path = "output.csv"

# planets_df.to_csv(file_path, index = False)

# print(f"Dataframe has been printed to {file_path}")

#------------------- Activity 3 - Adding to the dataframe -----------------


data = {
    'Name': ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'],
    'Average Temperature (°C)': [167, 464, 14, -60, -108, -139, -197, -200],
    'Radius (km)': [2439.7, 6051.8, 6371.0, 3389.5, 69911.0, 58232.0, 25362.0, 24622.0],
    'Color': ['Gray', 'Yellowish-white', 'Blue and green', 'Red', 'Orange with white bands', 
              'Yellow with brownish hues', 'Pale blue', 'Deep blue'],
    'Interesting Feature': [
        'Mercury has the most extreme temperature variation in the solar system.',
        'Venus has a surface temperature that is hotter than Mercury’s, despite being farther from the Sun.',
        'Earth is the only known planet to support life.',
        'Mars is home to the tallest volcano in the solar system, Olympus Mons.',
        'Jupiter is the largest planet in the solar system and has a giant storm, the Great Red Spot.',
        'Saturn is famous for its spectacular ring system, made mostly of ice and rock.',
        'Uranus rotates on its side, with its axis tilted over 90 degrees.',
        'Neptune has the strongest winds in the solar system, reaching speeds of up to 2,100 km/h.'
    ]
}

new_data = {
    'Discovered By': [
        'Known since ancient times', 'Known since ancient times', 'Not applicable', 
        'Known since ancient times', 'Known since ancient times', 'Known since ancient times', 
        'William Herschel', 'Johann Galle and Urbain Le Verrier'
    ],
    'Year Discovered': [
        'Unknown', 'Unknown', 'Not applicable', 'Unknown', 'Unknown', 'Unknown', '1781', '1846'
    ],
    'Composition (Main Elements)': [
        'Iron, Silicate', 'Carbon dioxide, Nitrogen', 'Nitrogen, Oxygen, Silicon, Iron', 
        'Iron, Magnesium, Silicon, Oxygen', 'Hydrogen, Helium', 'Hydrogen, Helium', 
        'Hydrogen, Helium, Methane', 'Hydrogen, Helium, Methane'
    ]
}

data.update(new_data)

planets_df = pd.DataFrame(data)

#------------------ Activity 4 - Adding Pluto ------------------
pluto_data = {
    'Name': ['Pluto'],
    'Average Temperature (°C)': [-229],
    'Radius (km)': [1188.3],
    'Color': ['Light brown with shades of white and red'],
    'Interesting Feature': ['Pluto has a heart-shaped glacier called Tombaugh Regio, and it’s part of the Kuiper Belt.'],
    'Discovered By': ['Clyde Tombaugh'],
    'Year Discovered': [1930],
    'Composition (Main Elements)': ['Nitrogen, Methane, Carbon monoxide (on the surface), with possible rocky and icy core']
}

pluto_df = pd.DataFrame(pluto_data)

planets_df = pd.concat([planets_df, pluto_df])

print(planets_df)