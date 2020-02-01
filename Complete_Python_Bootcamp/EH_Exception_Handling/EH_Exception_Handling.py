###### SECITON  10 EH- Exception Handling

### Lets start by viewing an example of some error that may occur:
### Consider the following function

def add(num1,num2):
    return num1+num2

print(add(10,20))

### No problems here. However, consider asking for user input to to ask for num2 in the above function
num1 = 10
# num2 = input("Please provide a number: ") ## If the user inputs a number from the keyboard, the input function
                                          ## will interpret it as a String and thus the add function will NOT return
                                          ## a TypeError

## A very common error indeed! Whatever happens after THIS line of code WILL NOT BE executed.
print(add(num1,10))

## Instead we use a try-except block. Even if there is an error, execution of the script is NOT halted.
## Consider the follwing example:

try:
    ##Attempt this code, however it may have an error
    result = 10 + 10

except:
    print("Hey, it seems you are not adding correctly!") ## Code execution is not halted. The Error is handled here
                                                         ## Gets executed when try fails.

else: ##Try-except-else -> A block of code to be executed if there is no exception. Gets executed when try succeeds.
    print("Add went well ")
    print(result)

