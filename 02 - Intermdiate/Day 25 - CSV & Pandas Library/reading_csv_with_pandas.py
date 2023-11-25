import pandas as pd

data = pd.read_csv("weather_data.csv")
print(type(data["temp"]))
# Pandas Series, Single Column in the table. (day : series) (temp : series) ....
print(type(data))
# DataFrame Should be considered like a sheet on Excel or google sheets
print("-" * 25)

data_dict = data.to_dict()  # DataFrame to Dictionary
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)
print("-" * 25)

# Average (Mean) of temperatures

avg = sum(temp_list) / len(temp_list)
print(avg)

# OR
print(data["temp"].mean())
print("-" * 25)

# Max
print(data["temp"].max())
print("-" * 25)
# Get Data from rows
print(data[data["day"] == "Monday"])
print(data[data["temp"] == data["temp"].max()])
print("-" * 25)
# Conditional Selection

monday = data[data["day"] == "Monday"]  # Creating a Pandas series from the DataFrame
monday_temp = monday["temp"]
monday_temp = (monday_temp * 9/5) + 32  # Celsius to fahrenheit
print(monday_temp)