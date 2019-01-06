## DICTIONARIES 2 IN PYTHON ##
import datetime

name = str(input(">> Your name: "))
entrada = int(input(">> Cant of values in dictionary: "))

my_dictionary = {"Hello":name}

#Starting loop for with x that is less than the entered variable
for x in range(entrada):
    #Enter two item
    item = input("Value of item 1: ")
    item2 = input("Value of item 2: ")
    my_dictionary[item]=item2#Enter two item for our dictionary
    print("\n")#line break

#Convert to list our dictionary
#list(my_dictionary)
#print(">>My dictionary: ",sorted(my_dictionary.values()))#Sorted values of our dictionary

print(">>My dictionary: ",my_dictionary)
print(">> Loading loop for...")
#traveling our dictionary created
for x,y in my_dictionary.items():
    if x == "Hello" and y == name:
        continue
    print("- English: ",x,"- Spanish: ",y)

#print farewell with user name
print(">> Goodbye,",my_dictionary["Hello"])

hora = datetime.datetime.now()
print(">> HORA Y FECHA DE SESION: ",hora)
