import sys

#######################
# This program was written by Victor Lopez on 5/26/2019
# Copyright Programming in Python 3 A Complete Introduction to the Python Language by Mark Summmerfield
# Solution to exercise 1 chapter 1

Zero = ["  ***  ",
        " *   * ",
        "*     *",
        "*     *",
        "*     *",
        " *   * ",
        "  ***  "]

# Digits contents
One = [" * ", "** ", " * ", " * ", " * ", " * ", "***"]
Two = [" *** ", "*   *", "*  * ", "  *  ", " *   ", "*    ", "*****"]
Three = ["*****", "    *", "    *", "*****", "    *", "    *", "*****"]
Four = ["   *  ", "  **  ", " * *  ", "*  *  ", "******", "   *  ", "   *  "]

Five = ["*****", "*    ", "*    ", "*****", "    *", "    *", "*****"]
Six = ["*****", "*    ", "*    ", "*****", "*   *", "*   *", "*****"]

Seven = ["*****", "    *", "   * ", "  *  ", " *   ", "*    ", "*    "]
Eight = [" *** ", "*   *", "*   *", " *** ",  "*   *",  "*   *", " *** "]
Nine = [" ****", "*   *", "*   *", " ****", "    *", "    *", "    *"]


# Declare Digits Variable
Digits = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]


# Process the input
try:
    # digits=sys.argv[1]  # To try it from the command line uncomment this line and comment the next two lines

    # Works both for the command line and IDE's
    msg = "Input an integer: "
    digits = input(msg)

    row = 0
    while row < 7:
        line = ""
        column = 0
        while column < len(digits):
            number = int(digits[column])
            digit = Digits[number]

            for symb in digit[row]:
                if symb == " ":
                    line += symb
                elif symb == "*":
                    line += str(number)
            line += "  "
            column += 1
        print(line)
        row += 1
except IndexError:
    print("usage: bigdigits.py")
except ValueError as err:
    print(err)
