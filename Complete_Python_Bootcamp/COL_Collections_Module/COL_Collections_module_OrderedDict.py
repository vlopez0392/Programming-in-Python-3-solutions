###################################### SECTION 15 - Advanced Python Modules ############################################
########################### OrderedDict

from collections import OrderedDict

### An OrderedDict is a dictionary subclass that remembers the order in which the elements are added.
### Dictionaries are mappings and DO NOT remember the order in which the keys and values are added.

### A "regular" dictionary
d = {}
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
d['e'] = 5
d['f'] = 6
d['g'] = 7
print(d)

### Printing the items in a regular dictionary
for k,v in d.items():
    print(k,v)

### Consider the OrderedDict
d = OrderedDict()
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
d['e'] = 5
d['f'] = 6
d['g'] = 7
print(d)

for k,v in d.items():
    print(k,v)

### Testing equality in an OrderedDict
### In a regular dictionary order of addition is not relevant
d1 = {}
d1['a'] = 1
d1['b'] = 2

d2 = {}
d2['b'] = 2
d2['a'] = 1

print(d1 == d2)

### In an Ordered Dictionary order of addition IS relevant
d1 = OrderedDict()
d1['a'] = 1
d1['b'] = 2

d2 = OrderedDict()
d2['b'] = 2
d2['a'] = 1

print(d1 == d2)