# ENSF 592 Spring 2021
# June 3 Lab 9
# Exercises
 
import numpy as np
import pandas as pd

# Example continued from Lab 6/7/8
# Refer to the weather data stored in Lab9Data.xlsx


# Demo: creating/exporting a multi-dimensional DataFrame from Excel

#all_data = pd.read_excel(r".\Lab9Data.xlsx")
#all_data = pd.read_excel(r".\Lab9Data.xlsx", index_col=[2,5])
all_data = pd.read_excel(r".\Lab9Data.xlsx", index_col=[2,5,6,7])

print(all_data)

#all_data.to_excel(r"./Lab9DataExport.xlsx", index = True, header = True)

print(all_data.index)

# Add a column to calculate the delta for day (difference between max and min)

all_data["Delta"] = all_data["Max Temp (°C)"] - all_data["Min Temp (°C)"]

print(all_data)

# Find the average measurements for each month (across both years)

print(all_data.mean(level = 'Month'))

# Print the data in both locations on May 1, 2021

print(all_data.loc[:,2021,5,1])
