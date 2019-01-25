# PYTHON FILE WRITE #

#Create a new File: 
# To create a new file in Python, use the open() method, with one of the
# following parameter:
#       "x" - Create - will create a file, returns an error if the file exist
#       "a" - Append - will create a file if the specified file does not exist 
#Example:
#        Create a file called "demofile.txt"
"""
myFile = open("demofile.txt","x")
"""
#or
#Example: Create a new file if it does not exist:
"""
myFile = open("demofile.txt","w")
"""

#Write to an Existing File: 
# To write toan existing file, you must add parameter to the open() function:
#   "a" - Append - will append to the end of the file
#   "w" - Write - will overwrite any existing content

#Example: 'Open the file "demofile.txt" and append content to the file'

f = open("\PYTHON - DE - 0 - 10000\Modulo 3 - File Handling\demofile.txt","x") #create file
f.write("Now the file has one more line!")#write file
f = open("\PYTHON - DE - 0 - 10000\Modulo 3 - File Handling\demofile.txt","r") #read file
print(f.read())       
