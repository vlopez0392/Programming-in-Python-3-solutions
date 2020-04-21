###################################### SECTION 15 - Advanced Python Modules ############################################
########################### timeit
import timeit

### Let's time how long does creating the string '0-1-2-...-99' takes

###Method 1 - Joining a large string
t1 = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
                                                                    ##First argument is the method you want to time
print(t1)                                                           ##Second argument is the number of times to run

### Method 2 - List comprehension
t2 = timeit.timeit('"-".join([str(n) for n in range(100)])', number = 10000)
print(t2)

### Method 3 - Map function
t3 = timeit.timeit('"-".join(map(str,range(100)))', number = 10000)
print(t3)

#### When using a jupyter notebook you can use the magic function %timeit, number of loops need not be specified.