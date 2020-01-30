####OOP HOMEWORK

#PROBLEM 1:
#Fill in the Line class method to accept coordinates as a pair of tuples and return the slope and
#distance of the line.

import math
class Line:
    def __init__(self,coor1,coor2):
        self.x1, self.y1 = coor1
        self.x2, self.y2 = coor2

    def distance(self):
        return math.hypot((self.x1-self.x2), (self.y1-self.y2))

    def slope(self):
        return ((self.y1-self.y2)/(self.x1-self.x2))

coor1 = (1,2)
coor2 = (4,6)

myLine = Line(coor1,coor2)

print("Coordinate 1: " + str((myLine.x1, myLine.y1))  + " Coordinate 2: " + str((myLine.x2, myLine.y2)))
print("Line distance to origin: ", myLine.distance()) ### Must print 5
print("Line slope: ", myLine.slope())    ### Must print 1.3333

print('=='*50, '\n')

# PROBLEM 2:
# Fill in the cylinder class:

class Cylinder:
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return math.pi*(self.radius**2)*self.height

    def surface_area(self):
        return 2*(math.pi*(self.radius**2)+math.pi*self.radius*self.height)

### Consider the default parameters:
cylinder = Cylinder()

print("Cylinder 1: " + "Radius: " + str(cylinder.radius) + " Height: " + str(cylinder.height))
print("Cylinder surface area: ", cylinder.surface_area())
print("Cylinder volume: ",       cylinder.volume())

print('=='*50, '\n')

### Consider r = 3, h = 2
cylinder2 = Cylinder(2,3)

print("Cylinder 2: " + "Radius: " + str(cylinder2.radius) + " Height: " + str(cylinder2.height))
print("Cylinder surface area: ", cylinder2.surface_area())
print("Cylinder volume: ",       cylinder2.volume())