### OOP (Part IV)
### Special Methods

### Special methods allow us to use built-in Python operations such as the len() function or the print() function
### with our own user created objects.

### Checking the length of a built-in data type (list)
mylist = [1,2,3]
len(mylist)

### Can we do the same for our own user defined objects?
### Consider the following simple class:

class Sample():
    pass

sample = Sample()

#len(sample) ##Throws a type error
print(sample) ## Prints the location of the object in memory

### To do so, we must use special (magic/dunder) methods:
### Let's try with another class:

class Book():
    def __init__(self, title, author, pages):
        self.title =  title
        self.author = author
        self.pages  = pages

    ##Special methods start and end with double underscore
    #a.
    def __str__(self):
        return f"{self.title} by {self.author}"

    #b.
    def __len__(self):
        return self.pages

    #c
    def __del__(self): ##Decreases the object references to the object by 1 (Not the object itself !!!). The object is
                       ##then set for garbage collection if and only if the object has no references. However, this is
                       ##not guaranteed to happen (i.e. Non-determnistic).
        print("A book reference has been deleted") ##We may add additional functionality

b = Book("Python Rocks", "Vick", 200)
print(b) ##Since Book now has a String representation defined (special str method) we obtain a nicer output.
print(str(len(b)))
b
