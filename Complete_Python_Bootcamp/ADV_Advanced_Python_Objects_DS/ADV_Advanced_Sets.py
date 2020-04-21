################################ SECTION 16 - Advanced Python Objects & DS #############################################
########################### Advanced Sets

#### In this lecture we will explore several advanced methods for sets.
s =set()

#### Adding elements to a set
s.add(1)
s.add(2)
s.add(2) ##Repeated elements are not allowed in a set!
print(s)

#### Removing the elements of a set
s.clear()
print(s) ##Empty set

#### Copying a set
s = {1,2,3}
sc = s.copy()

#### Difference methods - Useful! Returns the difference between two and more sets
s = {1,2,3,4}
print(s)
print(sc)
print(s.difference(sc))

# Difference update -> Method returns all the elements from set1 after removing same elements that were found in set 2
s1 = {1,2,3}
s2 = {1,4,5}
s1.difference_update(s2)
print(s1) ### The variable is modified permanently!

#### Discard methods -> discard() removes an element in a set if its a member
s = {1,2,3,4}
s.discard(2) ##If the discarded element is in the set, it is discarded, if not, the original set is returned.

#### Intersection methods - Intersections return a new set with the common elements in two or more sets
s1 = {1,2,3,45,65,64}
s2 = {1,45,78,65,23}
print(s1.intersection(s2))

# Intersection update will update set with the intersection of a itself and another set. Again the set is modified
#                                                                                        permanently.
s1.intersection_update(s2)
print((s1))

#### isdisjoint() - Returns True if two sets have a NULL intersection or no elements in common
s1 = {1,2}
s2 = {1,2,4}
s3 = {5}

print(s1.isdisjoint(s2)) ## Returns False since s1 and s2 have elements in common
print(s1.isdisjoint(s3)) ## Returns True since  s1 and s3 have no elements in common

#### issubset() - Returns True if set1 is contained in set2
print(s1.issubset(s2))

#### issuperset() - Returns True if set1  contains set2
print(s2.issuperset(s1))
print(s1.issuperset(s2)) ##False

#### Symmetric difference - Returns all the elements that are exactly in ONE of the sets. The update version behaves
#                                                                                         as usual.
print(s1.symmetric_difference(s2))

#### Union method - Returns all of the elements that are in either set
print(s1.union(s3)) #{1,2,5}

#### Update method - Updates a set with the union on another set
print(s1)
s1.update(s3)
print(s1)