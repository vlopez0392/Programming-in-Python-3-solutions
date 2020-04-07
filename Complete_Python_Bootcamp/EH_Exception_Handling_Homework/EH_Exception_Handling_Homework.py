#### SECTION 10 - EH_Exception_Handling_Homework

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
### PROBLEM 1
### Handling the exception of the following block of code using a try-except block:
try:
    for i in ['a','b','c']:
        print(i**2)
except TypeError:
    print("Found a Type Error")

print('=='*50)

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
### PROBLEM 2
### Handling the exception of the following block of code using a try-except-finally block:

try:
    x = 5
    y = 0
    z = x/y
except ZeroDivisionError:
    print("Division by zero Error")
finally:
    print("All done")

print('=='*50)

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
### PROBLEM 3
### Write a function that asks for an integer and prints the square of it. Use a while loop with a try, except, else
### block to account for incorrect inputs.

def return_squares():
    while True:
        try:
            num = int(input("Please enter the integer to be squared: "))
        except TypeError:
            print("Sorry, that is not an integer, try again")
            continue
        else:
            num2 = num**2
            print("Your integer: " + str(num) + " |-|-|-|-|-|-| The square of your integer: " + str(num2))
            print("All done!")
            break

return_squares()