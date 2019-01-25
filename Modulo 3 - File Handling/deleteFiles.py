# PYTHON DELETE FILE #

# DELETE A FILE: To delete a file, you must import the OS module, and runs its os.remove function:
# Example:
#          Remove the file "demofile.txt"

"""
import os
os.remove("demofile.txt")
"""
#Check if File exist: To avoid  getting an error, you might want to check if the file exist before you
#try to delete it.
#Example: 'Check if file exist, then delete it.

"""
import os

#delete a file

if os.path.exists("\PYTHON - DE - 0 - 10000\Modulo 3 - File Handling\ teamo.txt "):
    os.remove("\PYTHON - DE - 0 - 10000\Modulo 3 - File Handling\ teamo.txt")
    print("delete")
else:
    print("no delete")
"""

"""
#delete a dir
if os.path.exists("\PYTHON - DE - 0 - 10000\Modulo 3 - File Handling\Demo File"): #File route
    os.rmdir("\PYTHON - DE - 0 - 10000\Modulo 3 - File Handling\Demo File") #File route to delete
    print("Folder delete")
else:
    print("Folder no exists") #if no exists the directory
"""


"""
try:
    import os
except:
    print("Something went wrong..")
options = ["Create File (0)","Read File (1)","Write File (2)","Delete File (3)","List Dirs (4)"]
print("///////////////////////////////////////////////")    
print("///////////         MANAGER FILE        ///////")
print("///////////    By: @DeveloperJoseph     ///////")     
print("///////////////////////////////////////////////")
for x in options:
    print(">> ",x)

enterUser = int(input("#> Chosen Number: "))#enter user
if enterUser == 0:
    print("\n///////////////////////////////////////////////")
    print("////////////      CREATE FILE        //////////")
    print("///////////////////////////////////////////////")

    optionCreateFile = ["Create file (0)","Create folder(1)"]
    for x in optionCreateFile:
        print(">> ",x)
    enterOption = int(input("Enter option to create: "))
    if enterOption  == 0:
        nameFile = str(input("#> Enter File Name or url(): "))
        extension = str(input("#> Extension of File(.txt,.pdf,etc): ."))
        try:
            myFile =  open("\PYTHON - DE - 0 - 10000\Modulo 3 - File Handling\ "+str(nameFile)+"."+str(extension),"x")
        except:
            print(">> Something went wrong..")
        print(">> File created... ")
        writeFile = str(input("Write your file (y/n): "))
        if writeFile == 'y':
            enterWrite = str(input("Write in your file: "))
            myFile.write(enterWrite)
        elif writeFile == 'n':
            print(">> Thanks..")
    elif enterOption == 1:
        nameFile = str(input("#> Enter Folder Name or url(): "))
        try:
            os.makedirs(nameFile)
        except:
            print("Something went wrong..")
        print(">> Thanks..")
"""    
    
