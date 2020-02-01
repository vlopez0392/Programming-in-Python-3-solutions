#### This module will be call mymodule.py and its method myfunc(). The results will be displayed in the terminal.
### This can be thought of as a main program. We will also call some modules from several packages.

### Importing from a module
from mymodule import myfunc
myfunc()

### Importing from packages
from MyPackage import some_mainfile
from MyPackage.Subpackage.subscript import sub_report

### Calling a function from their fully qualified package names
some_mainfile.report()

### Calling the function directly. This function has been imported previously with the syntax:
### from package.module import module_function
sub_report()
