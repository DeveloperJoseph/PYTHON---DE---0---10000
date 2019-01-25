#PYTHON FILE OPEN #

#Open a File on the server:
#Asume we have the following file, located in the same folder as Python:
############################################################################
# >> Demofile.txt: Hello! Welcome to demofile.txt
#                  This file is for testing purposes.
#                  Good Luck!!
############################################################################

#To open the file, use the built=in open() function
#The open() function returns a file object, which hasa a read() method for
#reading the content of the file.
"""
f = open("demofile.txt","rt")
print(f.read())
"""

#Read only parts of the File:
#By default the read() method returns the whole text, but you can also specify 
#how many character you want to return:
#Example: 'Returns the first characters of the file:
"""
f = open("\PYTHON - DE - 0 - 10000\Modulo 1\helloworld.txt","r")
print(f.read(5))
"""

#Read Lines: You can return one line by using the readline() method.
#Example: 
#         'Read one line of the file'
"""
f = open("\PYTHON - DE - 0 - 10000\Modulo 1\helloworld.txt","r")
print(f.readline())
"""
#By calling readline() two times, you can read the two first lines:
"""
f = open("\PYTHON - DE - 0 - 10000\Modulo 1\helloworld.txt","r")
print(f.readline())
print(f.readline())
"""
#By looping through the lines of the file, you can read the wole file,
#line by line:
#Example: 'Loop through the file line by line'
"""
f = open("\PYTHON - DE - 0 - 10000\Modulo 1\helloworld.txt","r")
count = int(input("Number: "))
for x in range(count):
    print(f.readline())
"""

import os
entries = os.listdir("E:\PYTHON - DE - 0 - 10000\Modulo 3 - File Handling")
print(entries)