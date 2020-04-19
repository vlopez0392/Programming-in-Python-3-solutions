###################################### SECTION 15 - Advanced Python Modules ############################################
########################### namedtuple

###### A regular tuple
t = (1,2,3)
print(t[0]) ##We can use indexing to grab elements from that tuple - For most cases this is enough

### However, remembering which index to use is sometimes hard, you may not know the indices associated with each tuple
### field.

### namedtuple - Assigns both an index and a name to each element of a tuple -> Somewhat like a mini class.

from collections import namedtuple

##Think of this as a new class
Dog = namedtuple('Dog', 'age breed name') ## Arguments: 'Name of the namedtuple', ' A string of attributes separated
                                          ## space in a single string

### Creating a namedtuple - Creates a new object type
vick = Dog(age = 2, breed = 'lab' , name = 'Vick')

## Calling attributes and methods
print(vick.age)
print(vick.breed)

## Another example
Cat = namedtuple('Cat', ' fur claws name')
c = Cat(fur='fuzzy', claws = False, name = 'Kitty')
print(c.claws)
print(c[0]) ## Can also call by index

