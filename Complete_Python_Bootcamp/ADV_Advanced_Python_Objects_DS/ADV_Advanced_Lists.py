################################ SECTION 16 - Advanced Python Objects & DS #############################################
########################### Advanced Lists

######## In this lecture we will explore some additional methods for lists.

#### Append - Adds elements to the end of a list
l = [1,2,3]
l.append(4)
print(l)

#### Count - Count the number of times an element appears on a list
c1 = l.count(10)
print(c1)

c2 = l.count(2)
print(c2)

#### Extends vs append - Extends will extend a list with the elements of another list, however, it will do so without
#                        inserting these elements as a list, e.g.

l1 = [5,6]
l.extend(l1)
print(l)

# Append on the other hand will append these elements as a list. Let's say the appended 4th element will be a list.
l = [1,2,3,4]
l.append(l1)
print(l)

#### Index - The index() method returns the index of the element placed as the argument
print(l.index(2))
# print(l.index(10)) # Returns a ValueError since the value 10 is not in the list

#### Insert - Inserts the element in the second argument at the position specified by the first argument
l.insert(2, "inserted")
print(l)

#### Pop - Pops the last element in the list, in place!
l.pop(0)
print(l)

#### Remove - Removes the first occurrence of the element in the argument
l1 = [1,2,3,4,5,3]
l1.remove(3)
print(l1)

#### Reverse - Reverses the list in place
l1.reverse()
print(l1)

#### Sorts - Sorts the element in place ()
l1.sort()
print(l1)