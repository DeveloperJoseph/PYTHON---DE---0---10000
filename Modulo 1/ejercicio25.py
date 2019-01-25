##Python RegEx ##
#A RegEx, or Regular Expression, is a sequence of characters
#that forms a search pattern.

#RegEx Module:
#Python has a built-in package called re, which can be used to work with
#Regular Expressiones.

#Import the 're' module:
import re
import datetime
#RegEx in Python:
#When you have imported the 're' module, you can start using 
#regular expressions.
#Example:
    # Search the string to see if it starts with "The" and ends
    # with "Spain"
   
text = "The 2 rains in Spain"
"""
x = re.search("^The.*Spain$",text)
print("Yes! We have a match..") if (x) else print("No! We haven't a match..")  
"""

#RegEx Functions:
#The 're' module offers a set of functions that allows us to search a
#string for a match:

# Function->    # Description->
# 'findall'     -   (Returns a list containing all matches)
# 'search'      -   (Returns a Match Object if there is a match anywhere in the string)
# 'split'       -   (Returns a list where the string has been split at each match)
# 'sub'         -   (Replaces one or many matches with a string)

#Metacharacters:
#Are characters with a special meaning:

# Character->          # Description->                # Example-> 
#   []          -    A set of characters                 [a-m]
"""
x = re.findall("[a-n]",text) 
print(sorted(x,reverse=True))#Sorted values
"""
#   \           - Signals a special sequence              \d
#                 (can also be used to escape
#                 special characters)

"""
x = re.findall("\d",text) # '\d' digits or '\s' strings
print(x)
"""

#Special Sequences:
#A special sequence is a \ followed by one of the characters
#int the list below, and has a special meaning: \A \n \B \d \D \s

#Sets:
#A set is a set of characters inside a pair of square brackets[] with
#a special meaning: [arn][a-n][^arn][0123]

#The search() Function:
#- This function searches the string for a match, and return a Match Object
#  if there is a match.
#- If there is more than one match, only the first occurrence of the match will be
#  returned.
#Example:
    # Search for the first white-space character in the string:
    # Note: If no matches are found, the value 'None' is returned.
"""    
x = re.search("\s",text)
print("The first whote-space character is located in position: ",x.start())
"""

#The split() Function:
#Returns a list where the string has been split at each match.
#Example:
#       Split at each white-space character:   
"""
x = re.split("\s",text)
print(x)
"""
#You can control the number of occurrences by specifying the
#'maxsplit' parameter.
#Example:
    # Split the string only at the first occurrence:
"""
x = re.split("\n",text,1)
print(x)
"""
#The sub() Function:
#Replaces the matches with the text of your choice.
#Example:  
    #Replace every white-space character with the number 9
"""    
x = re.sub("\s","*",text)
print(x)
"""
#You can control the number of replacements by specifying the
#'count' parameter.
#Example:
"""
x = re.sub("\s", "9", text, 2)
print(x)
"""

#Match Object:
#Is an object containing information about the search and the result.
#Note: If there are no match, the value None will be returnted, instead of the Match Object.
#Example: 
    # Do a search that will return a Match Object:
"""
x = re.search("ai",text)
print(x)
"""
#The Match Object has properties andn methods usted to retrieve information about the search, and the result:
# .span()  = 'returns  a tuple containing the start , and end positions of the math.'
# .string = 'returns the string passed into the function.'
# .group() = 'returns the part of the string where there was a match'
#Example 1: 
    # Print the positions(start and end positions) of the first match  ocurrence.
    # The 'RegEx' looks for any word that start with an upp case "S".
"""
x = re.search(r"\bS\w+",text)
print(x.span())   

"""
#Example 2:
    # Print the string passed into the function
"""
x = re.search(r"\bS\w+",text)
print(x.string)
"""
#Example three:
    # Print the part of the string where there was a match,
    # The regular expression looks for any words that start with an upper case "S"
"""    
x = re.search(r"\bS\w+",text)
print(x.group())
"""
#Note: If there are no match, the value None will be returned, instead of the Match Object.

"""
#Other library of date and time
import arrow
utc = arrow.utcnow()
local = utc.to('US/Pacific')
print("Datetime with arrow: ",local.humanize())
"""

"""
#Example one
name = str(input("Enter your name: "))
last_name = str(input("Enter your last name: "))

default_lastName = "Sanchez"
replace=  re.sub("de la cruz",default_lastName,last_name)
print(name+" "+replace) if last_name  == "de la cruz" or last_name=="DE LA CRUZ" else print(name+" "+last_name)
"""

"""
#Example two >
def main(x):
    for d in x:
        print(d)
    print("> Fin...")    

data = input("Enter a data: ")       
print(main(data))     
"""
