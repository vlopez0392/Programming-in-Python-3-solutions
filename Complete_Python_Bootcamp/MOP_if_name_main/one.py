##one.py

### Calling a python script from the command line/Terminal -> Calling python one.py runs everything at indentation level
### 0 (methods and classes).
### In Python, unlike other languages,  there is no main() function that serves as entry point to your program.
### Instead, implicitly all code at indentation level 0 is run when you call the script file.

### Python has a built-in variable called __name__ (Note the underscores! BUILT-IN)
### This variable gets assigned a String. When you run the script directly, __name__ is assigned a valuie of "__main__".
### All of this is done in the background.

def func():
    print("func() in one.py")

print("Indentation level 0 at one.py")

if __name__ == '__main__': ##Means RUN the script
    print("one.py was run directly")
else:
    print("one.py was imported")