## PYTHON FILE OPEN ##
# File handling is an important part for any web application.
# Python has several functions for creating, reading, updating, and deleting files.

#File Handling:
# The key function for working with files in Python is the open() function.
# The open() function takes two parameters; filename , and mode.
# The are four different methods (modes) for opening a file:
#   "r" - Read - Default value. Opens a file for reading, error if the file does not exit.
#   "a" - Append - Opens a file for appending, creates the file if it does not exit.
#   "w" - Write - Opens a file for writing, create the file if it does not exit.
#   "x" - Create - Creates the specified file, returns an error if the file exists.

# In addition you can specify if the file should be handled as binary or text mode.
#   "t" - Text - Default value. Text mode.
#   "b" - Binary - Binary mode(e.g images).

# Syntax:
# To open a file for reading it is enough to specify the name of the file:
f = open("demofile.txt")
#The code above is the same as:
f = open("demofile.txt","rt")
#Because "r" for read, and "t" for text are the default values, you do need to specify them.
#Note: Make sure the file exists, or else you will get an error.


"""
f = open("\PYTHON - DE - 0 - 10000\Modulo 1\helloworld.txt","rt")
print(f.read()," Services of Cybersecurity")
"""