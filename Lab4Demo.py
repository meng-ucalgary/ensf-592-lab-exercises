# ENSF 592 Spring 2021
# May 18 Lab 4
# Documentation Demo Exercise

# General notes:
# Docstrings start after the function/class declaration, not above it.
# You are free to use whichever docstring format you prefer (Google, Numpy, etc.) as long as you are consistent through your program.
# See bottom of file for syntax for printing out your docstring.


# THIS COMMENT GETS REMOVED WHEN DOCSTRING IS USED
# get_user_input prompts for any input entry and returns the input value and its type
# Argument: Takes in a number to count which input prompt is being given
# Returns the input value (str object) and its corresponding type (type object)
def get_user_input(n):
    """Prompts for any input entry and returns the input value and its type
    
        Parameters:
            n (int): A positive integer to count which input prompt is being given

        Returns:
            entry (str): The string input received from the user 
            type(entry): The type of the input

    """
    entry = input("Please type any entry #" + str(n + 1) + ": ")
    print(type(entry))
    print(type(type(entry)))
    return entry, type(entry)


# process_user_input prints a value that was previously input and its type
# Argument: Takes in a number to count which input prompt is being printed, the original input value, and the type of the value
# No return value
def process_user_input(n, entry, type):
    print("This is entry #" + str(n + 1) + ":", entry)
    print("The type of entry #" + str(n + 1) + " is :", str(type))


# Method 1:
# Print a new line for spacing and then the method title
print('\n')
print("***METHOD 1***")
# Prompt the user to enter their name, input function will return the value as a string
input1 = input("Please enter your name: ") # Prompts for input
print("This is the first input:", input1) # Prints the original input back to the terminal along with a statement


# Method 2: continuous input via a while loop
print('\n' * 2) # Print two lines for spacing
print("***METHOD 2***")

# Loop continuously until "x" is provided as the input
while True:
    input2 = input("I am looking for specific input. You must type x: ") # Prompt for user input
    if input2 == "x":
        break
print("This is the second input: " + input2) # Print original value to user


# Method 3: call functions
print('\n' * 2) # Add header for spacing
print("***METHOD 3***")
num_of_repeats = 3  # set number of inputs to prompt for
results = [] # create empty list to store inputs
results_types = [] # create list for types

# Call get_user_input three times, add values to the list for input and its corresponding type
for i in range(num_of_repeats):
    a, b = get_user_input(i)
    results.append(a)
    results_types.append(b)

# Call process_user_input, pass input counter, the actual input, and the type of that input
for i in range(num_of_repeats):
    process_user_input(i,results[i], results_types[i])



# Print out our documentation from get_user_input function above!
print(get_user_input.__doc__)
