################################ SECTION 16 - Advanced Python Objects & DS #############################################
########################### Advanced Python test

#### Problem 1
n = 1024
hx = hex(1024)
bn = bin(1024)
print("{0} converted to hexadecimal is: {1} and converted to binary is {2}".format(n,hx,bn))

#### Problem 2
n = 5.23222
print(round(5.23222,2))

#### Problem 3
s = "hello how are you Mary, are you feeling okay?"
print("Is the string s" + s + " in lowercase? " + str(s.islower()))

#### Problem 4
s = "twywywtwywbwhsjhwuwshshwuwwwjdjdid"
print("Count of w's in the letter s" + s + " : " + str(s.count('w')))

#### Problem 5
my_set1 = {2,3,1,5,6,8}
my_set2 = {3,1,7,5,6,8}

print("Elements in set 1 the are not in set 2: " + str(my_set1.difference(my_set2)))

#### Problem 6
print("Elements that are either in set 1 or set 2: " + str(my_set1.union(my_set2)))

#### Problem 7 - {0:0, 1:1, 2:8, 3:27, 4:64}
d = {x:pow(x,3) for x in range(5)}
print(d)

#### Problem 8
l = [1,2,3,4]
lold = l.copy()
l.reverse()

print("Reverse of the list {0}: {1}  ".format(lold,l))

#### Problem 9
l   = [3,4,2,5,1]
lold = l.copy()
l.sort()
print("Sorting the list {0}: {1}  ".format(lold,l))


