import pandas as pd
import csv

# Painful way to read csv files (Wrong)
with open("weather_data.csv", mode='r') as file:
    data = file.readlines()
    print(data)

print("-" * 25)

# Import the csv module and read the content of the file in csv format
with open("weather_data.csv", mode='r') as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":  # excluding the column name with an if statement
            temperatures.append(int(row[1]))  # typecasting all the strings to integers and append to list

print(temperatures)
print("-" * 25)

# This method also painful if we work with huge csv files :(

###########################################
# Working with very big csv or huge dataset
###########################################

dataframe = pd.read_csv("weather_data.csv")
print(dataframe)
