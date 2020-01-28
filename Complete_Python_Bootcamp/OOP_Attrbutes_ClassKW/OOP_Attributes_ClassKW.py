### OOP (PArt I)
### Using OOP to create our own objects
### THe built-in data types are objects in Python, e.g.
mylist = [1,2,3]

### We can call many methods, such as append, on this list object:
mylist.append(1)
print(mylist)

### Keep in mind that everything in Python is an object
### Therefore, we are able to check the type of our objects

print(type(mylist)) ### mylist is of type list

### We can use the Class keyword to create our own objects:
''' A class serves like a blueprint to construct our objects and their nature. 
    Then, we can instantiate our objects based on the blueprint provided 
    by the class '''

### Consider the following example:

class Dog(): ##CamelCased! First letter is Capitalized!

    ##__init__ is called whenever when we instantiate the class. Its our constructor.
    def __init__(self, breed, name, spots): ## self represents the instance of the object itself
                                            ## In Python, self is passed explicitly into the constructor.
        self.breed = breed                  ## Declares and assigns the breed attribute of our dog.

        ###Defining other attributes (Notice the attribute types may vary - MUST BE DOCUMENTED!)
        self.name = name
        self.spots = spots ##Type control can be enforced by other means (Later)

#### Lets instantiate the Dog class given a breed parameter
myDog = Dog(breed = 'Lab', name = 'Sammy', spots = False)

#### We can now print the attributes of our myDog instance:
print(myDog.breed)
print(myDog.name)
print(myDog.spots)

#### Lets check the type of the Dog class
print(type(myDog))