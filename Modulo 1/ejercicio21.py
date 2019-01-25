#PYTHON CLASSES AND OBJECTS
#- Is an object oriented programming language.
#- Almost everything in Python is an object, with its properties 
#  and methods.
#- A class is like an object constructor, or a "blueprint" for creating
#  objects.

#Create a class:
#To create a class, use the keyword class:
#Example:
    # Create an object named p1, and print the value of x:
class myClass:
    x = 5

#Create object:
#Now we can use the class named 'myClass' to create objects:
#Example:
   # Create an object named p1, and print the value of x:
p1 = myClass()
print(">> Value of my class: ",p1.x)

#The __init__() Function:
#- The examples above are classes and objects in their simplest from,
#  and are not really useful in real life applications.
#- To understand the meaing of classes we have to understand the 
#  built-in __init__() function.
#- All classes have a function called __init__(), which is always
#  executed when the class is being initiated.
#- Use the __init__() function to assing values objects properties, or 
#  other operations that are necessaru to do when the object is being
#  created:

#Example:
    # Create a class named Person, use the __init__() function to assing
    # values for name and age:
class Animal:
    def __init__(self,name,age,color):
        self.name = name
        self.age = age
        self.color = color
    
    def myFunction(self):
        print("- Raza: {}, Age: {} years, Color: {}".format(p1.name,p1.age,p1.color))


name = str(input(">> Raza: "))
age = int(input(">> Age: "))
color = str(input(">> Color: "))
p1 = Animal(name,age,color)

#QUOTE: The __init__() function is called automatically every time the
#class is being used to create a new object.

#Object Methods:
#- Can also contain methods. Methods in objects are functions thar belongs
#  to the object.
#- Let us create a method in the Animal class:
#Example:
    #Insert a function , and execute it on the p1 object:
print("=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>")
p1.myFunction()
print("=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>")
#Quote: The self parameter is a reference to the class instace itself,
#and is used to acces varibales that belongs to the class.

#The Self Parameter:
#- Is a reference to the class itself, and is used to access variables that
#  belongs to the class.
#- It does not have to be named self, you can call it whatever you like, but
#  it has to be the first parameter of any functions in the class:


#Modify Object Properties:
# You can modify properties on objects like this:
#Example:
    # Set the age of p1 to 40:
#p1.age = 40

#Delete object properties:
# You can delete properties on object by using the del keyword:
#Example:
    # Delete the age property from the p1 object:
#del p1.age

#Delete Objects:
# You can delete objects by using the del keyword:
#Example: Delete the p1 object:
#del p1
