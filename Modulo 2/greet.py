# Importing the module 'hello.py'
import hello as hello

"""
print(hello.say_hello.__doc__)
name = str(input("What's your name?: "))
print(hello.say_hello(name))...
"""
print("\n")

#Creating an object of our class 'hello.py'
name = str(input("Name: "))
country = str(input("Country: "))
age = int(input("Age: "))

user_information = hello.user_information(name,country,age)
print("I'm ",user_information.name)
print("I'm from ",user_information.country)
print("I'm ",age,' years old')
 