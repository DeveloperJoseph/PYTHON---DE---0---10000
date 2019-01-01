# Importing the module 'hello.py'
import hello as hello

"""
print(hello.say_hello.__doc__)
name = str(input("What's your name?: "))
print(hello.say_hello(name))...
"""
print("\n")

#Data Entry:
name = str(input("Name: "))
country = str(input("Country: "))
age = int(input("Age: "))

#Creating an object of our class 'hello.py'
user_information = hello.user_information(name,country,age)

#Data output
print("\nI'm ",user_information.name)
print("I'm from ",user_information.country)
print("I'm ",user_information.age,' years old')
print("More Information: ",user_information.calc_age())
 