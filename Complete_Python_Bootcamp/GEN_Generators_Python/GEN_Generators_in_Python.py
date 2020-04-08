############################################ SECTION 13 - Python Generators ############################################

#### A normal/regular function (NO use of generators)
def create_cubes(n): ###Useful when you need a list
    result = []
    for x in range(n):
        result.append(x**3)
    return result

print(create_cubes(10)) ##When using the create_subes() function, you keep the entire list in memory!

### EXAMPLE 1
### What happens if you only want to print each result? e.g.

for x in create_cubes(10): ##Still creates a list of numbers held in memory
    print(x) ##But this time, we only needed one value at a time

print("################################# \n")

### We just need the previous value and the formula to create this value
### Let's see how to use a generator

def generate_cubes(n): ## This is a generator!
    for x in range(n):
        yield x**3  ### We only yield the last value each time it is used -> THis is much more memory efficient

for x in generate_cubes(10):
    print(x)

print("################################# \n")

### EXAMPLE 2 - Generating a Fibonnacci Sequence
def gen_fibon(n):
    a = 1
    b = 1
    for j in range(n):
        yield a
        a,b = b, a+b

#### Equivalent function using a list (Less efficient!)
def gen_fibon(n): ### If we want to iterate through a sequence it is better to use the yield keyword
                  ### It is best to use a generator if we are dealing with values that only get used once
                  ### (As in the print function) -> No need to store the whole range of values
    a = 1
    b = 1
    output = []
    for j in range(n):
        output.append(a)
        a,b = b, a+b

    return output

##### EXAMPLE 3 - Using the next and iter keywords -> Not used as often, used internally!
def simple_gen():
    for x in range(3):
        yield x

for number in simple_gen():
     print(number)

print("################################# \n")

##### Using the next() function
g = simple_gen()
print(g) ## g is a generator object

### We can ask for the next value of g using the next function
print(next(g)) ##Internally, the generator object has the behavior as that of the yield keyword
print(next(g))
print(next(g))

##print(g) raises a StopIteration Error -> All of the values have been yielded
                                    ##  -> The for-loop catches this and stops iterating when next returns None

print("################################# \n")

##### Using the iter() function -> Converts an iterabel object into an iterator

s = 'hello'
## We cannot call next() on s -> s is NOT an iterator but a String object
## We cannot directly iterate over a String

## Thus, we call the iter() function to convert our String into an Iterator

s_iter = iter(s)
print(next(s_iter)) #prints 'h'