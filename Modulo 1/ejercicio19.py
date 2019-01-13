## FUCTIONS AND RECURSION IN PYTHON ##
#A function is a block of code which only runs when it
#is called. You can pass data, known as parameters, into
# a function. A function can return data as a result.

## CREATING A FUNCTION:
#In python a function is defined using the 'def' keyword.
def myFunction():
    print("Hello from a function.")

def multiplicate(x,y):
    """ Return one value , multiplicate (x*y) """
    return x * y

def suma(x,y):
    """ Return one value , adition (x*y) """
    return x + y

def greet(name, age,lastName="Sanchez"):
    #condition for the value of 'lastName'
    if lastName == "":
        lastName="Sanchez"
    #condition for the value of 'age'    
    if age >0 and age<=17:
        state = "Menor de edad"
    elif age >=18 and age<=130:
        state = "Mayor de edad" 
    else:
        state =  "Edad no válida"  
    print("Name Complete: {} {}, Age: {} ('{}')".format(lastName,name,age,state))


## CALLING A FUNCTION CREATED:
#To call a function, use the function name followed by
#parenthesis. 
print("\n")
myFunction()
name = str(input("Your name: "))
lastName = str(input("Your last Name: "))
age = int(input("Age: "))
greet(name,age,lastName)


"""
value1 = int(input(">>Value 1: "))
value2 = int(input(">>Value 2: "))
print(multiplicate.__doc__)
print("-Result: ",multiplicate(value1,value2),"\n") 

user_input = str(input(">>See help of (suma or multiplicate): "))
user_input.lower()
if user_input == "suma":
    print(help(suma))
elif user_input == "multiplicate":
    print(help(multiplicate))
else:
    print(">>Input not valid...")
"""
"""
def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k-1)
        print(result)
    else:
        result = 0
    return result

entered_number=int(input(">> Enter a number: "))
print(tri_recursion(entered_number))
"""
