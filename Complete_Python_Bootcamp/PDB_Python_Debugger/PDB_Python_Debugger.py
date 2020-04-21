###################################### SECTION 15 - Advanced Python Modules ############################################
########################### Python Debugger - pdb

#### You've probably used several print statements to find errors in your code, but a better way to find bugs and
#### errors is to use the python debugger or pdb module
import pdb

#### Python debugger module - Implments an interactive debugging environment within python programs and includes
#### features such as : - Pause your program, - Look and verify values of variables
###                     - Watch program execution step by step

#### Implementing pdb by creating a bug on purpose

x = [1,3,4]
y = 2
z = 3

#### We set a pdf trace here - The code will run up until here
#### An interactive debugging environment will run. We can check variable values and perform operations.
pdb.set_trace()
### To quit the pdb environment type q

result = y+z
print(result)

#result2 = y+x ##Catching errors like this in a larger codebase is more difficult.
#print(result2)