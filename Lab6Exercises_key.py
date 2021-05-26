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

may_2021 = [
12.9,	1,	    7,
10.8,	1,	    5.9,
13.3,	-1.5,	5.9,
12.5,	2.4,	7.5,
14.3,	1.7,	8,
19.7,	2.7,	11.2,
16.5,	5.8,	11.2,
5.8, 	0.5,	3.2,
2.9, 	0.4,	1.7,
13.6,	-3,	    5.3,
15.7,	-1.4,	7.2,
17.8,	0.2,	9,
16.8,	6.5,	11.7,
19.4,	2.4,	10.9,
22.3,	3.7,	13,
25.1,	10.1,	17.6,
27.2,	10.3,	18.8,
16.8,	6.6,	11.7,
7.5,     0.8,	4.2,
2.8,    -1.8,	0.5,
11.3,	0.1,	5.7,
13.8,	-0.5,	6.7,
10.6,	1.8,	6.2
]

may_2020 = [
15.2,	0.5,	7.9,
19.6,	-0.1,	9.8,
16.7,	1.8,	9.3,
6.8,	2.3,	4.6,
16.3,	-1,	    7.7,
16.4,	1.3,	8.9,
16.5,	6,	    11.3,
10.9,	3.8,	7.4,
13.7,	-0.4,	6.7,
7.1,	0.5,	3.8,
8.1,	-0.5,	3.8,
10.4,	1.9,	6.2,
15.8,	-0.3,	7.8,
17.3,	3.2,	10.3,
18.1,	2.3,	10.2,
21.8,	3,	    12.4,
21.6,	6,	    13.8,
19.9,	8.9,	14.4,
14.4,	8.2,	11.3,
11.7,	7.8,	9.8,
8.2,	2.7,	5.5,
5.3,	2.9,	4.1,
15.6,	4.7,	10.2
]

may_2019 = [
7,	    -2.4,	2.3,
10.8,	-0.5,	5.2,
8.5,	-0.4,	4.1,
-0.2,	-2.5,	-1.4,
2.8,	-3.4,	-0.3,
12.5,	-3.7,	4.4,
11.4,	0.2,	5.8,
12.3,	2.2,	7.3,
17.4,	1.7,	9.6,
19.3,	7.1,	13.2,
23.6,	0.7,	12.2,
21.4,	11.5,	16.5,
19.2,	5.6,	12.4,
20.2,	8.3,	14.3,
17.5,	8.1,	12.8,
8.3,	5.7,	7,
7.4,	2.7,	5.1,
6.7,	2.1,	4.4,
11.3,	2,	    6.7,
9.9,	-1.7,	4.1,
7.6,	4,	    5.8,
17.9,	3.2,	10.6,
20.7,	5.3,	13
]

array_2021 = np.array(may_2021).reshape((23,3))
array_2020 = np.array(may_2020).reshape((23,3))
array_2019 = np.array(may_2019).reshape((23,3))

may_data = np.array([array_2021, array_2020, array_2019])

print("Full set of data from days 1 to 23 in May 2021, May 2020, May 2019:")
print(may_data)

# Split the array into separate arrays for each week (7 days each, except for the last one).

week1, week2, week3, week4 = np.split(may_data, [7, 14, 21], axis=1)

print("Data for May 1st to 7th:\n", week1)
print("Data for May 8th to 14th:\n", week2)
print("Data for May 15th to 21st:\n", week3)
print("Data for May 22nd to 23rd:\n", week4)

# Use the split arrays to update the mean value on May 11th, 2020 to be 4.2
# Are the split arrays copies or views of the original data array?

week2[1,3,2] = 4.2  # Choose the 2nd array "layer", 4th row down, 3rd column

print("Revised Data for May 8th to 14th:\n", week2)
print("Check for changes to all data:\n",may_data)

# Create an array where the order of the weeks is reversed (i.e. May 22nd to 23rd, then May 15th to 21st, then May 8th to 14th, then May 1st to 7th).
# Check that the original data array is not impacted.

reverse_weeks = np.hstack([week4, week3, week2, week1])
# reverse_weeks[0,0,0] = 100        # test for changes to original data
print("Reverse Week Order:\n", reverse_weeks)
print("Check for changes to all data:\n",may_data)

# Reorder the original data array to reverse the order of the years and the days, but not the order of the measurements.

reverse_years_days = may_data[::-1, ::-1]

print("Reversed Years and Days:\n",reverse_years_days)
print("Check for changes to all data:\n",may_data)
