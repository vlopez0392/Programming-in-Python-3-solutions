################################ SECTION 16 - Advanced Python Objects & DS #############################################
########################### Advanced Numbers
##### In this lecture: Other number representations and advanced built-in methods for numbers in Python

##### Decimal numbers -> Hexadecimal numbers - Use the hex() function
print(hex(246))
print(hex(512))

##### Decimal to Binary Conversion - Use the bin() function
print(bin(1234))
print(bin(128))
print(bin(512))

##### Built-in functions - Python also has a built-in math library in case you require more advanced mathematical
#####                      operations.

#### 1 - Using pow() to compute power of numbers
# A. With two arguments
print(pow(2,4)) ## 2**4 = 16

# B. With three arguments
print(pow(2,4,5)) ## (2**4)%3 = 1

#### 2 - Using the absolute value function
print(abs(-50))

#### 3 - Using the round() function
print(round(3.45)) ## The second argument specifies the number of digits after the decimal point.




