################################ SECTION 16 - Advanced Python Objects & DS #############################################
########################### Advanced Strings

###### String objects have a variety of methods to add functionality and save time! Lets explore them:
s = 'hello world'

###### 1 - Changing cases
### Capitalizes the first letter of each word in a string
print(s.capitalize())

### Uppercases every letter in a String
print(s.upper())

### Lowercases every letter in a String
print(s.lower())


###### 2 - Location and counting methods
### Counts the number of occurrences of the argument in the count() method
print(s.count('o'))

#### Finds the first instance (from left to right) of a letter
print(s.find('h'))


###### 3 - Formatting methods - Not used as ofter
### Centers the string around a filler string with a certain length
print(s.center(50, 'z'))

### Expand tabs method - Useful when parsing through a lot of text data - Again not used as often
s2 = 'hello\thi' ## \t is a escape character for a tab
print(s2)

s2.expandtabs() ##Does exactly the same without the need to call the print() function

### Check if the string is some sort of case - Quite useful for NLP
s = 'Hello'

### isalnum() -> Check if all characters in s are alphanumeric
print(s.isalnum())

### isalpha() -> Checks if all the characters in a string are alphabetic
print(s.isalpha())

### islower() -> Checks if all cased characters in s are lower and if there is at least one cased character in s
print(s.islower())

### isupper() -> Checks if all cased characters in s are upper and if there is at least one cased character in s
print(s.upper().isupper())

### isspace() -> Returns True if all characters in s are whitespace
print(s.isspace())

### istitle() -> Only returns True if the string is a Title cased string -e.g. This Is A Title - THiS is NoT
print("This Is A Title".istitle())
print("This Is NOt A TiTle".istitle())

### endswith() -> Checks if a String ends with the argument character
print(s.endswith('o'))

### Which is equivalent to
print(s[-1] == 0)

###### 4 - Built-in regex operations

### split(element) -> Used to split the String at a certain element(s) (every occurrence) and return a list of the result
print(s.split('l'))

### partition() -> Searches for the separator in S and returns the separator, the part after and before it.
###             -> If the separator is not found, return S and two empty strings

print(s.partition("l"))
print(s.partition('j'))
