# ENSF 592 Spring 2021
# May 20 Lab 5
# Exercises

# Solve the exercises provided in main.

# Some documentation is included as an example (in Google Style). The documentation is not complete!
# All methods should have their own docstrings unless otherwise specified (i.e. __init__ and  properties)
# The specifics of other formats may vary- you may choose whichever format you prefer as long as you are consistent.

import re

class Horse:
    """A class used to create Horse object.

        Attributes:
            age (int): Integer that represents the horse's age
            colour (str): String that represents the horse's colour
            breed (str): String that represents the horse's breed
            ***Note that self is implicit and is not included!

    """

    sci_name = "Equus caballus"
    """sci_name (str): Class variable with default string value of "Equus caballus"
    """

    def __init__(self, name, age, colour, breed):
        self.__name = name 
        self.__age = age
        self.__colour = colour
        self.__breed = breed


    # define all private instance variables as properties to get getters/setters

    @property #decorator
    def name(self):
        return self.__name

    @property #decorator
    def colour(self):
        return self.__colour

    @property #decorator
    def age(self):
        return self.__age

    @property #decorator
    def breed(self):
        return self.__breed

    # define any customized getters/setters
    @age.setter
    def age(self, new_val):
        return self.__age

    # define instance methods
    def print_all_stats(self):
        print("""{0} stats: Age = {1}, Colour = {2}, Breed = {3}.""".format(self.name, self.age, self.colour, self.breed))

    # define class methods
    @classmethod
    def horse_info(cls):
        print("The scientific name of a horse is: " + Horse.sci_name)


class Rider:
    
    def __init__(self, name, age, horse):
        self.name = name
        self.age = age
        self.horse = horse

    def print_all_stats(self):
        print("""{0} stats: Age = {1}, Horse Age = {2}, Horse Colour = {3}, Horse Breed = {4}."""
        .format(self.name, str(self.age), str(self.horse.age), self.horse.colour, self.horse.breed))        


def main():
    print("\n***Horse and Rider Program***\n")

    # Create five horses and five riders.

    horse1 = Horse("Blaze", 14, "bay", "Morgan")

    rider1 = Rider("Alex", 34, horse1)


    # Exercise 1
    # Collect all horse and rider ages and create a single set that lists each number that appears at least once.
    # A large competition is planned for 5 years from now. All riders must be over 20, but under 50. Horses must be over 10 and under 25.
    # Create a single generator function that can be used to find which horses and riders will be eligible for the competition.


    # Exercise 2
    # Use a regular expression to find all competition-eligible horses and riders with names containing both "A/a" and "L/l"


    # Exercise 3:
    # Customize the setter for age by adding an exception. 
    # Age must be set to a value greater than zero, otherwise a message is printed to the user using a ValueError exception.


if __name__ == '__main__':  # optional in Python 3
    main()


