########################################
        # PYTHON DICTIONARIES #
    #    - DEVELOPER JOSEPH  -     #
########################################

#Definition:
   #A dictionary is unordened, changeable and indexed. 
   #In Python dictionaries are written with curly brackets,
   #and they have keys and values.

#Example:

#Create and print a dictionary
print("\n#> Loading course of Create and print a dictionary in Python....")
thisdict = {"brand":"Ford","Model":"Mustag","year":1964}
print("> Dictionary : "+str(thisdict))

#Accesing Items:
#You can access the items of a dictonary by  referring to 
#its key name, inside square brackets.

#Example: "Get the value of the 'model' key":
print("\n#> Loading course of Get the Value from a dictionary in Python....")
x = thisdict["year"]
print('> Get value -> '+str(x))
# OR
x = thisdict.get("brand")
print('> Get value two -> '+str(x))


#Change values:
#You can change the value of a specific item by referring
#to its key name.

#Example: "Change the values of the 'dictionary created' ":
print("\n#> Loading course of Change the values of the dictionary in Python....")
thisdict["brand"]='Suzuki'
thisdict["Model"]="S-10"
thisdict['year'] = 2017
print("> New dictionary: "+str(thisdict))

#Loop Through a Dictonary:
#You can loop through a dictionary by using a for loop:
#When looping through a dictionary, the return values are the
#key of the dictionary, but there are method  to return the 
#values as well:

#Example: "Print all key names in the dictionary, one by one":
print("\n#> x")
for i in thisdict:
    for j in thisdict:
        print("Key values -> "+str(i)+": "+str(thisdict[j]))
    break

# OR

# JOSEPH TRANSLATE  #
print("\n#> Loading Joseph Translate, please wait...")
languages = {"Spanish":"Hola","English":"Hello","Russian":"привет","Chinese":"你好"}

#ADDING ITEMS:
#Adding an item to the dictionary done by using a new index key and assigning a
#values to it.
languages["Arab"]="مرحبا"
languages["Croatia"]="Bok"
languages["Hindi"]="नमस्ते"
print("# Download external files for new languages translated...")

#Check if Key Exists:
#To determine if a specified key is present in a dictionary use the
#in keyword.
if "Spanish" in languages:
    print("#> State Language Spanish: OK")
    if "English" in languages:
        print("#> State Language English: OK")
        if "Russian" in languages:
            print("#> State Language Russian: OK")
            if "Chinese" in languages:
                print("#> State Language Chinese: OK")
                if "Arab" in languages:
                    print("#> State Language Arab: OK")
                    if "Croatia" in languages:
                        print("#> State Language Croatia: OK")
                        if "Hindi" in languages:
                            print("#> State Language Hindi: OK")

                   
print("> Numbers of languages translated: "+str(len(languages)))

#Loop Through a Dictonary more method languages.item():
for x, y in languages.items():
        print("Language: "+str(x)+"-> "+str(y))
        
print("\n>#Loading more languages translated....")
#Adding an item to the dictionary is done by using a 
#new index key and assigning a value to it:
languages["Italy"]="Ciao"
languages["Vietman"]="Xin chào"
print("# Download external files for new languages translated...")

#Loop Through a Dictonary more method languages.item():
for z, w in languages.items():
    print("Language: "+str(z)+"= "+str(w))
print("> Languages translated: "+str(len(languages)))

#Removing Items:
#There are several methods to remove items from a dictionary:

#Example: "The pop() method removes the item with the specified
#key name."
#> Removing one Item from my languages dictionary 
print("\n## Removing one Item method pop()...")
print("Item delete: "+str(languages.pop("Croatia")))
print("## Removing las Item method popitem()...")
print("#> Random Item removing is: "+str(languages.popitem()))
print("## Loading New List...")
print(">+ List of languages: "+str(languages))

# The clear() keyword empties the dictionary:
languages.clear()

#Using variable languages as constructor
languages = dict(Animal="Perro",Name="Firulay's",Age=3)
print("> New Constructor dict is: "+str(languages))

#The copy() method returns a copy of the specified dictionary.
#Copy the constructor languages in new variable languages2
print("\n#> Copy the constructor languages in new variable languages2...")
languages2 = languages.copy()
print("#> Add new item Estado in languages2....")
languages2["State"]=None
print("> Output new dictionary languages2:"+str(languages2))#print console contructor languages2
print("#> Active state of dictionary languages2...")
languages2["State"]=1
print("> Output new dictionary languages2:"+str(languages2))#print console contructor languages2

#Definition and Usage
#The fromkeys() method returns a dictionary with the specified keys and values.
print("\n>#Loading The fromkeys() method ..... ")

#create 3 variables
k = ("Animal1","Aminal2","Animal3")
new_k_dictionary = dict.fromkeys(k)
print("> New constructor 'k' "+str(new_k_dictionary))
print("## Update values from new_k_dictionary....")
new_k_dictionary["Animal1"]=3
new_k_dictionary["Aminal2"]=4
new_k_dictionary["Animal3"]=5
print("## Loading cycle for in new_k_dictionary......")
for a,b in new_k_dictionary.items():
    print("> The "+str(a)+" has "+str(b)+" years old.")
    
            
print("\n> Thank you for attention..!!")



        



