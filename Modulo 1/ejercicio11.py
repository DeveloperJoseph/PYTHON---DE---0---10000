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

thisdict = {"brand":"Ford","Model":"Mustag","year":1964}
print("Dictionary : "+str(thisdict))

#Accesing Items:
#You can access the items of a dictonary by  referring to 
#its key name, inside square brackets.

#Example: "Get the value of the 'model' key":
x = thisdict["year"]
print('Get value -> '+str(x))
# OR
x = thisdict.get("brand")
print('Get value two -> '+str(x))


#Change values:
#You can change the value of a specific item by referring
#to its key name.

#Example: "Change the values of the 'dictionary created' ":
thisdict["brand"]='Suzuki'
thisdict["Model"]="S-10"
thisdict['year'] = 2017
print("New dictionary: "+str(thisdict))

#Loop Through a Dictonary:
#You can loop through a dictionary by using a for loop:
#When looping through a dictionary, the return values are the
#key of the dictionary, but there are method  to return the 
#values as well:

#Example: "Print all key names in the dictionary, one by one":
for i in thisdict:
    for j in thisdict:
        print("Key values -> "+str(i)+": "+str(thisdict[j]))
    break

# OR

# JOSEPH TRANSLATE  #
print("#> Loading Joseph Translate, please wait...")
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


                   
print("Numbers of languages translated: "+str(len(languages)))

for x, y in languages.items():
        print("Language: "+str(x)+"-> "+str(y))
        



