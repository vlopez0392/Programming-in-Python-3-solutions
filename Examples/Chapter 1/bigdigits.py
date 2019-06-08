import sys

#######################
# This program was written by Victor Lopez on 5/26/2019
# Copyright Programming in Python 3 A Complete Introduction to the Python Language by Mark Summmerfield
# Example 1 in Chapter 1

Zero = ["  ***  ",
        " *   * ",
        "*     *",
        "*     *",
        "*     *",
        " *   * ",
        "  ***  "]

One = [" * ", "** ", " * ", " * ", " * ", " * ", "***"]
Two = [" *** ", "*   *", "*  * ", "  *  ", " *   ", "*    ", "*****"]
Three = ["*****", "    *", "    *", "*****", "    *", "    *", "*****"]
Four = ["   *  ", "  **  ", " * *  ", "*  *  ", "******", "   *  ", "   *  "]

Five = ["*****", "*    ", "*    ", "*****", "    *", "    *", "*****"]
Six = ["*****", "*    ", "*    ", "*****", "*   *", "*   *", "*****"]

Seven = ["*****", "    *", "   * ", "  *  ", " *   ", "*    ", "*    "]
Eight = [" *** ", "*   *", "*   *", " *** ",  "*   *",  "*   *", " *** "]
Nine = [" ****", "*   *", "*   *", " ****", "    *", "    *", "    *"]

Digits = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]

try:
    digits = sys.argv[1]  # To try it from the command line uncomment this line and comment the next two lines
    # msg = "Input an integer: "
    # digits = input(msg)

    row = 0
    while row < 7:
        line = ""
        column = 0
        while column < len(digits):
            number = int(digits[column])
            digit = Digits[number]
            line += digit[row]+"  "
            column += 1
        print(line)
        row += 1

except IndexError:
    print("usage: bigdigits.py")
except ValueError as err:
    print(err)
