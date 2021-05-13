# ENSF 592 Spring 2021
# May 13 Lab 3
# Exercise 1

# Add comments to explain the functionality of this program


def get_user_input(n):
    entry = input("Please type any entry #" + str(n + 1) + ": ")
    return entry, type(entry)

def process_user_input(n, entry, type):
    print("This is entry #" + str(n + 1) + ":", entry)
    print("The type of entry #" + str(n + 1) + " is :", str(type))


# Method 1: ask once
print('\n')
print("***METHOD 1***")
input1 = input("Please enter your name: ")
print("This is the first input:", input1)


# Method 2: continuous input via a while loop
print('\n' * 2)
print("***METHOD 2***")
while True:
    input2 = input("I am looking for specific input. You must type x: ")
    if input2 == "x":
        break
print("This is the second input: " + input2)


# Method 3: call functions
print('\n' * 2)
print("***METHOD 3***")
num_of_repeats = 3
results = []
results_types = []

for i in range(num_of_repeats):
    a, b = get_user_input(i)
    results.append(a)
    results_types.append(b)

for i in range(num_of_repeats):
    process_user_input(i,results[i], results_types[i])

