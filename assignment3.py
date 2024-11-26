import pandas as pd
import os

#---------------- Access Data -----------------

df = pd.read_excel("group_results.xlsx")

#---------------- Exploring the Data -------------------

# print(df.info())

# print(df.isnull().sum())

# print(df.describe())

#----------------- Analysing the Data --------------------

group_median_download = df['Median Download'].median()
print(f"Group Median Download Speed: {group_median_download:.2f} Mbps")

#---------------- Identifying Outliers -----------------

Q1 = df['Median Download'].quantile(0.25)
Q3 = df['Median Download'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[(df['Median Download'] < lower_bound) | (df['Median Download'] > upper_bound)]
print("Outliers in Median Download:")
print(outliers)

#-------------- Removing Outliers ---------------

df_cleaned = df[(df['Median Download'] >= lower_bound) & (df['Median Download'] <= upper_bound)]
cleaned_median_download = df_cleaned['Median Download'].median()
print(f"Cleansed Median Download Speed: {cleaned_median_download:.2f} Mbps")

#------------- Creating New Cleaned File (Using ChatGPT)-------------

# Load the original Excel file
file_path = os.path.join(os.getcwd(), 'group_results.xlsx')  # Directly get the file path

# Load the Excel file into a DataFrame
df = pd.read_excel(file_path)

# Define the path for the cleaned file (same directory, new filename)
cleaned_file_path = os.path.join(os.path.dirname(file_path), 'cleaned_group_results.xlsx')

# Check if the cleaned file already exists
if os.path.exists(cleaned_file_path):
    print(f"The file '{cleaned_file_path}' already exists. Skipping save.")
else:
    # Save the cleaned DataFrame to the new file
    df_cleaned.to_excel(cleaned_file_path, index=False)
    print(f"Cleaned data saved to {cleaned_file_path}")