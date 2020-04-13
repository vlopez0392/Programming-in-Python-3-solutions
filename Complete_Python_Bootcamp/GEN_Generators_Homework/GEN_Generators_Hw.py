############################################ SECTION 13 - Python Generators ############################################
import random

##### PROBLEM 1: Create a generator to generate the squares up until a number N
def generate_squares(N):
    for x in range(N):
        yield x**2

N = 11
for value in generate_squares(N):
    print(value)

print("################################# \n")

##### PROBLEM 2:Create a generator that yields “n” random numbers between a low and a high number
##### (that are the inputs).

def generate_rn(low, high, n):
    for i in range(n):
        yield random.randint(low, high)

N = 10
low = 13
high = 100
for value in generate_rn(low, high,N):
    print(value)

print("################################# \n")

##### PROBLEM 3: Use the iter() function to convert the String s = 'hello' into an iterator
s = 'hello'
gen_s = iter(s)

for letter in gen_s:
    print(letter)

print("################################# \n")

##### PROBLEM 4: Explain a use case generator using a yield statement where you would not want to use
##### a normal function with a return statement.

##### A generator would be used in the case where keeping all the values of an iterable in memory is not required.
##### e.g. Printing a value once, using a value once to generate the next value in a sequence.
##### In general, using generators with the yield statement is much more memory efficient than returning values
##### through a regular function.


##### PROBLEM 5:
##### Explain the use of gencomp in the code below.

my_list = [1,2,3,4,5]
gencomp = (item for item in my_list if item > 3)
for item in gencomp:
    print(item)

##### A generator comprehension is a simpler way of implementing a generator. A single line of code is required to
##### implement a GC.