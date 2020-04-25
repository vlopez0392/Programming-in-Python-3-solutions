################################ SECTION 16 - Advanced Python Objects & DS #############################################
########################### Advanced Dictionaries

##### We will explore a few more useful methods for dictionaries and we will study dictionary comprehensions
d1 = {'k1':1, 'k2':2}
print(d1)

#### A dictionary comprehension - Dictionaries also support comprehensions - Not as common as list comprhensions
d2 = {x:x**2 for x in range(10)} ##Key will be x and value will be x**2
print(d2)

#### What if we don't want to assign keys based on the values ?
d3 = {k:v**2 for k,v in zip(['a','b'],range(2,4))}
print(d3)

#### Iterations over key, values and items
for i in d1.items():
    print(i)

for v in d1.values():
    print(v)

for k in d1.keys():
    print(k)

#### We can also be items and values as follows:
print(d1.values())
print(d1.items())
print(d1.keys())
