# ENSF 592 Spring 2021
# May 25 Lab 6
# Exercises
 
import numpy as np

# Demonstration for creating multi-dimensional arrays

# Example 1 - auto-generated values
example1 = np.arange(27).reshape((3,3,3))
print("***Example 1***")
print(example1)
print("Shape =", example1.shape)
print("Number of dimensions =", example1.ndim)

# Example 2 - bring 2D arrays together
data1 = np.array( [ [1, 3, 5], [7, 9, 11] ] ) 
data2 = np.array( [ [2, 4, 6], [8, 10, 12] ] )
data3 = np.array( [ [-1, -3, -5], [-7, -9, -11] ] )
data4 = np.array( [ [-2, -4, -6], [-8, -10, -12] ] )

create3D = np.array([ data1, data2, data3, data4 ])
print("***Example 2***")
print(create3D)
print("Shape =", create3D.shape)
print("Number of dimensions =", create3D.ndim)
print("Value at [3, 1, 2] =", create3D[3, 1, 2])

create4D = np.reshape(create3D, (2, 2, 2, 3))
print("***Example 2 Reshape for 4 Dimensions***")
print(create4D)
print("Shape =", create4D.shape)
print("Number of dimensions =", create4D.ndim)
print("Value at [1, 1, 1, 2] =", create4D[1, 1, 1, 2])


# Practice Exercises

# Refer to the weather data stored in Lab6Data.xlsx
# Use NumPy to create and print a three-dimensional array where the rows are the dates, the columns are the temperature readings in Celsius, and the third dimension is each year from 2019 to 2021.


# Split the array into separate arrays for each week (7 days each, except for the last one).


# Use the split arrays to update the mean value on May 11th, 2020 to be 4.2
# Are the split arrays copies or views of the original data array?


# Create an array where the order of the weeks is reversed (i.e. May 22nd to 23rd, then May 15th to 21st, then May 8th to 14th, then May 1st to 7th).
# Check that the original data array is not impacted.


# Reorder the original data array to reverse the order of the years and the days, but not the order of the measurements.

