"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO: define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    minutes_remaining = EXPECTED_BAKE_TIME - elapsed_bake_time
    return minutes_remaining


#TODO: Define the 'preparation_time_in_minutes()' function below.
# To avoid the use of magic numbers (see: https://en.wikipedia.org/wiki/Magic_number_(programming)), you should define a PREPARATION_TIME constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations, and make changes to your code.
def preparation_time_in_minutes(number_of_layers):
    """Calculate preparation time in minutes.

    :param number_of_layers: int - number of layers added to lasagna.
    :return: int - total time spent to prepare the lasagna with the given number of layers.

    Function that takes the number of layers the lasagna has as an argument
    and returns the total time to prepare the lasagna with the given layers
    assuming each layer takes minutes as defined in PREPARATION_TIME to prepare .
    """
    total_time = number_of_layers * PREPARATION_TIME
    return total_time
    


#TODO: define the 'elapsed_time_in_minutes()' function below.
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate total time elapsed (preparation + baking) in minutes

    :param number_of_layers: int - number of layers added to lasagna.
    :param elapsed_bake_time: int - number of minutes the lasagna has spent baking in the oven already
    :return: int - total minutes in the kitchen - preparation + baking 

    Function that takes the number of layers of the lasagna and elapsed bake time
    as an argument and returns the total time spent in the kitchedn including preparation
    and baking time
    """
    
    prep_time = preparation_time_in_minutes(number_of_layers)
    total_time = prep_time + elapsed_bake_time
    return total_time
    

# TODO: Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)
