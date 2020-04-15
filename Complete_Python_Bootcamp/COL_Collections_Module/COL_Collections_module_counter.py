###################################### SECTION 15 - Advanced Python Modules ############################################
########################### Counter

#####Collections module -> Implements various specialized container datatypes
from collections import Counter

#### 1 - Counter
#### Counter is a dictionary subclass that allows you to count hashable objects.
#### Inside the counter the dictionary keys are the elements of the hashable object and the values are the count of
#### such objects.

l = [1,1,1,1,1,2,2,2,2,2,2,2,3,3,3,3,3,3,3,4,4,4,4,4,4,4,5,5,5,5,5,5,5]
print(Counter(l)) ##Count the values of a list - Acts like a dictionary

s = 'aassasasassauququqieie'
print(Counter(s))

### Counting the words in a sentence
sen = 'How many times does each word show up in this sentence ? word word show up up'
print(Counter(sen.split())) ## Useful for text parsing or NLP

###### Methods with counter

# Print most common values
c = Counter(sen.split())
most_common = c.most_common(3) ###Argument for n most common words n = 3
print(most_common)

# Sum all values
print(sum(c.values()))




