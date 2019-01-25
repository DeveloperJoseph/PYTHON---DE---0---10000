## PYTHON JSON ##
# - JSON is a syntax for storing and exchanging data.
# - JSON is text, written with Javascript object notation.

# JSON IN PYTHON:
#Python has built-in package called json, which can be use
#to work with JSON data.
#Example:
    # Import the json module:
import json

#Parse JSON - Convert from JSON to Python:
#If you have a JSON string, you can parse it by using the 
# json.loads() method.(The result will be a Python Dictionary)
#Example:
    # Conert from JSON to Python:
"""    
x = '{"name":"Joseph","age":17,"city":"New York"}' #some JSON
y = json.loads(x) #convert x string to y json
print(y["name"])#The result is a dictionary, and print value 'name' key
"""
#Convert from Python to JSON:
#If you have a Python object, you can convert it into a JSON string by
#using the json.dumps() method.
""""
x = {"name":"Joseph","age":17,"city":"New York"}
y = json.dumps(x)
print(y)
"""
#You can convert Python objects of the following types, into JSON strings:
"""
dict
list
tuple
string
int
float
True
False
None
#----------------------------------------#
#Example:
    # Convert Python object into JSON string, and print the values.

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
"""
#Example:
  # Convert a Python object containing all the legal data types:

legal_data = {
    "name":"Joseph",
    "age": 18,
    "married": False,
    "divorcied": False,
    "children": None,
    "pets": ('Cone', 'Candy'),
    "cars": [
        {"model":"BMW 230", "mpg": 27.5},
        {"model":"Ford Edge", "mpg": 24.1}
    ]

}

# Whitout format the result
"""print(json.dumps(legal_data))"""

#Format the result:
# - The example above prints a JSON string, but it is not very easy to
#    read, with no indentations and line breaks.
# - The json.dumps() method has parameters to make it easier to read the
#    result.
#Example:
    # Use the indet parameter to define the numbers of indents:
"""    
legalData_json = json.dumps(legal_data,indent=4)
print(legalData_json)
"""

#Order the result:
#The json.dumps() method has parameters to order the keys in the result:
#Example:
    # Use the sort_key parameters to specify if the result should be 
    # sorted or not:
print(json.dumps(legal_data,indent=3,sort_keys=True))