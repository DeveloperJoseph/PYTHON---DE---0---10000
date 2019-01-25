## Use a Module ##
#Now we can use the module we just created, by using the import 
#statement.
##Note: When using a function from a module,  use the 
# syntax: module_name.function_name.

from modulo import greeting,person #of my modulo imported its function 
import platform as plf #Re-naming a module

greeting("Joseph")
myAge = person["age"]#acceding the person dictionary of my 'module.py'
print(">> {} years".format(myAge))

os = plf.system
print("Your OS is: {}".format(os))

