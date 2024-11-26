import pandas as pd

df = pd.read_excel("first_hour_sales.xlsx")

df = df.set_index("Transaction ID")
df = df.drop(["Till ID", "Unnamed: 0"], axis = 1)
df = df.dropna(how = "any")
df = df.drop_duplicates()
df.at[15.0, "Cost"] = 6.00

def float_to_time(time_record):
    time_record = str(time_record)
    hours, minutes = time_record.split(".")
    timestamp = f"{int(hours):02}:{int(minutes):02}"
    return timestamp

df["Time"] = df["Time"].apply(float_to_time)

def split_basket(basket_string):
    items = basket_string.split(",")

    stripped_items = [item.strip() for item in items]
    return stripped_items

print(df)

