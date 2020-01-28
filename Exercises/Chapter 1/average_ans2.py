#######################
# This program was written by Victor Lopez on 5/26/2019
# Copyright Programming in Python 3 A Complete Introduction to the Python Language by Mark Summmerfield
# Solution to exercise 2 chapter 1

count = 0
curr_sum = 0
number_list = []
maximum = 0
minimum = 0

try:
    while True:
        line = input("Please enter an integer or press Enter to finish: ")
        if line:
            x = int(line)
            curr_sum += x
            count += 1
            number_list += [x]

            if len(number_list) == 1:
                maximum = x
                minimum = maximum
            else:
                for num in number_list:
                    if num > maximum:
                        maximum = num
                    elif num < minimum:
                        minimum = num
        else:
            break
except ValueError as err:
    print(err)

if count:
    print("numbers: " + str(number_list))
    print("count= ", count, "total= ", curr_sum, "mean= ", curr_sum/count, "maximum: ", str(maximum), "minimum: ", str(minimum))