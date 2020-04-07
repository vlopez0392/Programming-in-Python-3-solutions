###### SECTION  12 DEC- Decorators
###### Decorators Overview Part II

##### Functions as arguments/parameters
def hello():
    return "Hi Vick!"

def other_func(some_other_func): ###Passing a function as a parameter
    print("Other code goes here")
    print(some_other_func()) ### Passing a function as an argument

other_func(hello) ###Need to pass the raw hello function such that it can be called within other_func

print("#################################################### \n")

##### Coding a decorator - Realistically, no need to code this -> Used in Web Frameworks such as Django or Flask
def new_decorator(original_func):

    def wrap_func(): ###THis wrap_func represents the extra functionality you want to decorate your function with
        print("Some extra code, before the original function ")
        original_func()
        print("Some extra code, after the original function")
    return wrap_func

def func_needs_decorator(): ###We want to add extra functionality to this function with a decorator
    print("I want to be decorated!!")
    return " "

####We can use the new_decorator function to decorate the original function func_needs_decorator

decorated_function = new_decorator(func_needs_decorator) ###This is the manual way of implementing decorators
decorated_function()

print("#################################################### \n")

#### Using the @ syntax to implement decorators:

@new_decorator ## Comment this line to avoid calling the decorator
def func_needs_decorator(): ###We want to add extra functionality to this function with a decorator
    print("I want to be decorated more efficiently!!!")
    return ""

func_needs_decorator()