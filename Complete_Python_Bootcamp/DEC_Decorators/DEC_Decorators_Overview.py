###### SECTION  12 DEC- Decorators
###### Decorators Overview

##### In Python we can pass functions into other functions.
##### Consider the following function:
def func():
    return 1

print(func())
print(func) ###Prints the function location in memory, a function is also an object

##### Another function
def hello():
    return "Hello!"

print(hello())
print(hello)

###Let's assign the hello function to the greet variable:

greet = hello ###Now, is greet just pointing to hello or greet is a copy of the function by itself?

### Deleting hello
del hello
# print(hello()) ###The hello() function is no longer defined!

#### Testing greet
print(greet()) ### Still returns Hello! Greet is still pointing to the original hello function.
               ### Functions are objects that can be passed into other objects

print("#################################################### \n")

#### Passing functions into functions
### Consider the following function with a function definition:

def hello_Victor(name = 'Victor'):
    print("The Hello function has been executed")

    ### The scope of the following functions is limited to the hello() function
    def greet():
        return '\t This is the greet() function inside hello'

    def welcome():
        return '\t This is the welcome() function inside hello'

    ## Let's call greet
    print(greet())
    print(welcome())
    return "This is the end of hello"

#### Now, let's execute the hello() function and observe the behavior
print(hello_Victor())
print("#################################################### \n")

#### What if we want to access the greet() and welcome() functions?
#### Consider the following -  We will return a function:

def return_function(return_func = False):
    print("The Hello function has been executed")

    ### The scope of the following functions is limited to the hello() function
    def greet():
        return '\t This is the greet() function inside hello'
    def welcome():
        return '\t This is the welcome() function inside hello'

    print("I am going to return a function!")

    ### Returns the above defined functions
    if return_func:
        return greet
    else:
        return welcome

##### Now we can return a function and assign this function to a new variable OUTSIDE the scope of the original function
my_new_func_greet   = return_function(True)
my_new_func_welcome = return_function()

##### Let's see the results:
print(my_new_func_welcome())

print("#################################################### \n")
##### Another Example
def cool():
    def super_cool():
        return "I am vey cool!!!"

    return super_cool

are_you_cool = cool()
print(are_you_cool())