###################################### SECTION 15 - Advanced Python Modules ############################################
########################### defaultdict
from collections import defaultdict

#### 2- defaultdict
#### Is a dictionary like object which provides all methods provided by dictionary but takes first argument
#### (default_factory) as default data type for the dictionary. Using defaultdic is faster than using dict.set_default
####  method.

#### A defaultdic will never raise a KeyError. Any key that does not exist gets the value returned by the default
#### factory.

## A regular dictionary
reg_dic = {'k1':1}

print(reg_dic['k1'])
# reg_dic['a'] ##raises a KeyError
# A defaultdict

d = defaultdict(object) ##object is the default factory  // No keys in this dict
print(d['one']) ##We know have a key of 'one' -> Value returned is an object inb memory

for item in d:
    print(item)

#### We can use a defaultdict to initialize default values
d2 = defaultdict(lambda: 'none') ##This lambda function takes any argument (actually none) and always returns 'none'
print(d2['one'])
print(d2['two'])

print(d2) ## The keys whose values are not assigned will be assigned a default value of 'none' -> Use of the lambda
          ## function. The lambda function is the default condition.
