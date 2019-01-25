# PYTHON TRY - EXCEPT #
# The 'try' block lets you test a block of code for errors.
# The 'except' block lest you handle the error.
# The finally block lest you execute code, regardless of the result of the try - and
# except blocks.

# EXCEPTION HANDLING:
# WHhen an error occurs, or exception as well call it, Python will normally stop and 
# generate an error message.
# These exeptions can be handled using the 'try' statement.
#Example:
#       The 'try' block will generate an exception, because 'x' is not defined:
"""
try:
    print(x)
except:
    print(">> An exception occurred..")
"""
#Since the try block raises an error, the except bock will be executed.
#Without the try block, the program will crash and raise an error.
#Example:
#           This statement will raise an error, because x is not defined
"""
print(x)    
"""
#Many Exceptions:
#You can define as many exception block as yoo want, e.g if you want to execute a special block of 
#code for a special kind of error.
#Example:
#         Print one message it the try block raises a NameError and another for other error
"""
try:
    print(x)
except NameError:
    print("Variable x is not defined..")
except:
    print("Something else went wrong..")
"""
#ELSE: You can use the 'else' keyword to define a block of code to be executed if no
#errors were raised:
#Example: In this example, the 'try' block does not generated any error:
"""
try:
    print("Hello World")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")
"""

#Finally: The finally block, if specified , will be executed regardless if the
# try block raises an error or not.
"""
try:
    prin(x)
except: 
    print("Something went wrong")
finally:
    print("The 'try-except' is finished")
"""

#This can be useful to close objects and clean up resources
#Example: 
#         Try to open and write to a file that is not writable.
try:
    myFile = open("demofile.txt")
    myFile.write("This file is created by me, not writable")
except:
    print("Something went wrong when writing to the file")
finally:
    myFile.close()    
#The program can continye, without leaving the fule object open.

