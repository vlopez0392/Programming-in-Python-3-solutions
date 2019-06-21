import random

#######################
# This program was written by Victor Lopez on 5/26/2019
# Copyright Programming in Python 3 A Complete Introduction to the Python Language by Mark Summmerfield
# Example 2 in Chapter 1

# Define a function to get an int

def get_int(msg, minimum, default):
    while True:
        try:
            li_ne = input(msg)
            if not li_ne and default is not None:
                return default
            i = int(li_ne)
            if i < minimum:
                print("must be greater or equal than", minimum)
            else:
                return i
        except ValueError as err:
            print(err)


# Specify number of rows, columns, minimum and maximum values for random integers
rows = get_int("rows: ", 1, None)
columns = get_int("columns: ", 1, None)
minimum = get_int("Minimum or press Enter for 0: ", -1000000, 0)

default = 1000
if default < minimum:
    default = 2*minimum
maximum = get_int("maximum or press Enter for  " + str(default) + ": ", minimum, default)

# Processing
row = 0
while row < rows:
    line = ""
    column = 0
    while column < columns:
        j = random.randint(minimum,maximum)
        s = str(j)
        while len(s) < 10: # Add padding
            s = s + " "
        line += s
        column += 1
    print(line)
    row += 1