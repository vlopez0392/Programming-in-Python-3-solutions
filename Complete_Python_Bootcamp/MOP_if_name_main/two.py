##two.py
import one

print("Indentation level 0 at two.py")
one.func()

if __name__ == '__main__': ### Means RUN THE SCRIPT
    print("two.py was run directly")
else:
    print("two.py was imported")