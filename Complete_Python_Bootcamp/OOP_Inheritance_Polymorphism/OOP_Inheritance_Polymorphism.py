### OOP (Part III)
### Demonstrating the use of Inheritance and Polymorphism

### Inheritance: An OOP paradigm that consists in using already existing classes to
### define new classes.

### Benefits: - Reuse of code
###           - Reduces the complexity of a program

########################################################################################################################

### Inheritance ###
### Consider the following example:
### Base class (Inherited from class or parent class)

class Animal():
    def __init__(self):
        print("Animal created")

    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")

### Testing the functionality of our class
myAnimal = Animal()
myAnimal.eat()
myAnimal.who_am_i()

### Derived classes can use/inherit the methods defined in the base class
### Consider the following derived class:

class Dog(Animal): ##The base class is typed in parentheses after the derived class e.g. class Derive(Base)

    def _init__(self):
        Animal.__init__(self) ##The base class must be first created in the constructor of the derived class
        print("Dog created ")

    ## Methods from the parent class may be overridden by rewriting the method with the same method name and parameters:
    def who_am_i(self):
        print("I am a dog!")

    def eat(self):
        print("I am eating and I am a DOG")

    def bark(self):
        print("WOOF")

#### Instantiating the Dog Class (Derived) and using the inherited methods
myDog = Dog()
myDog.eat()
myDog.who_am_i()
myDog.bark()

print('=='*50, '\n')

#### Polymorphism ###

### Polymorphism: Refers to the way in which different classes can refer to the same method name. These methods can be
### called from the same place even though a variety of different objects may be passed in.

### Consider the following example with two classes:
class Dog():

    def __init__(self,name):
        self.name = name

    def speak(self):
        return self.name + " says WOOF!"

class Cat():

    def __init__(self,name):
        self.name = name

    def speak(self):
        return self.name + " says MEOW!"

#### Testing polymorphism (Example I) - When called, each object's speak method returns a result that is unique to the
#### object.
niko = Dog('Niko')
felix = Cat('Felix')

print(niko.speak())
print(felix.speak())

#### Testing polymorphism (Example II) -> Using a for-loop to iterate in a list of items, Items must have the same
###                                       callable methods for this to work.

for pet_class in [felix,niko]:
    print(type(pet_class))
    print(pet_class.speak())

#### Testing polymorphism (Example III)-> Using a function -> Common way to observe polymorphism

def pet_speak(pet): ## The parameter pet does not know the type of object it will receive.
    print(pet.speak())

##Again, the same method call provides results for each specific object.
pet_speak(felix)
pet_speak(niko)

#### Testing polymorphism (Example IV)-> Using abstract classed -> Classes that never expect to be instantiated.
##                                                              -> They are expected to be base classes.
## Consider the example:

class Animal():
    def __init__(self,name):
        self.name = name

    ## We don't expect to call this method
    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method ")

### Consider calling the speak() method given this abstract class (We're not supposed to instantiate it):
fred = Animal("fred")

#fred.speak() #Returns a NotImplementedError

##Instead, we must inherit from Animal:

class Parrot(Animal):

    def speak(self):
        return "I'm a parrot and my name is " + self.name

parrot = Parrot("Jerry")
print(parrot.speak())