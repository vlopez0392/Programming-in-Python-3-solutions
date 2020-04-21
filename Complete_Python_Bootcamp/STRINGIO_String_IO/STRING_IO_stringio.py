###################################### SECTION 15 - Advanced Python Modules ############################################
########################### StringIO

### The StringIO module implements an in-memory file like object. This object can then be used as input or output to
### most functions that you would expect a standard file object. Used widely in web scraping cases.

import io

### Arbitrary String
message = "This is a normal string"

### Use io.StringIO to set as file object
f = io.StringIO(message)

### Now we can treat the String as a file and use the methods associated with File IO like read and write.
print(f.read())
f.write(" Second line written to file like object")
print(f.seek(0))
print(f.read())
