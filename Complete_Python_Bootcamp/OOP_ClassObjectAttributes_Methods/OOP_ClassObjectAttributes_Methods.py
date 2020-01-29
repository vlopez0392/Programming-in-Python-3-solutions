### OOP (Part II)
### Using Class Object Attributes and Methods

########### EXAMPLE I

### Recall the dog class from last time:
class Dog():
    ##Some attributes of the dog will be the same regardless of the type of dog (e.g. always a mammal)

    species = "mammal" ## Class object attribute: An attribute that is the same for all instances of the class
                       ## No need to refer to self. COA -> Same for all objects of the class

    def __init__(self, breed, name, spots): ##User defined attributes.
        self.breed = breed
        self.name = name
        self.spots = spots

    ### Methods: Functions defined inside the body of the class used to perform operations that sometimes use
    ### the attributes of the class.

    ### OPERATIONS/ACTIONS --> Methods
    def bark(self, dogNumber): ## We can also add parameters to our methods
        return "WOOF! " + "My name is: " + self.name  + " and I am a "  + self.breed \
            + " WOOF!" + " I am dog number " + str(dogNumber) ## No need to call self. This parameter is provided by the
                                                              ## method call.
print('=='*50, '\n')
### Testing the class object attribute given to Dogs:
myDog = Dog(breed = 'Lab', name = 'Vick', spots = False)
myOtherDog = Dog(breed = 'Dalmatian', name = 'Bebi', spots = True)

### Both will print "mammal"
print(myDog.species)
print(myOtherDog.species)

### Calling methods on our objects
print(myDog.bark(1)) ### To execute our methods, we must add the parentheses after the method name.
print(myOtherDog.bark(2), '\n')

print('=='*50, '\n')

### EXAMPLE II

class Circle():
    ##Class object attributes
    pi = 3.14

    ##__init__ method ##
    def __init__(self, radius = 1): ### In this case, radius is defined as 1 by default
        self.radius = radius

        ### Attributes may be defined based on other attributes. NO need for an explicit parameter call.
        self.area = radius*radius*Circle.pi ##Class object attributes may be referenced from the name of the Class.

    ## Class methods
    def get_circumference(self):
        return self.radius*2*self.pi

### Checking the attributes and methods of the Circle class
myCircle = Circle(10)

print(myCircle.pi)
print(myCircle.radius)
print(myCircle.area)
print(myCircle.get_circumference())