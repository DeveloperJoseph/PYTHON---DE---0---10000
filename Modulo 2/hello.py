## Creating a module ##
#A module is a important file containing definitions and statements,
#also a module can be created by creating a .py file.

#Functions in a module can be used by importing the module.

def say_hello(x):
    """
    Este método que recibe un parametro(x),
    retorna un saludo join whit enter name
    """
    return "Hello "+str(x)
    
def say_emotion(x,y):
    print("Your age is: ",x)
    print("Your emotion is: ",y)

    
#For modules that your have made, they will need to be in the same
#directory as the file that you are importing them into.(However,
#you can also put them into the Python lib directory with the
#pre-included modules, but should the avoiled if possible.)

#Creating a class with name 'country', also has two variable 'peru_city'
#and 'united_state_city' in our class 'hello.py'
class user_information:
    def __init__(self,name,country,age):
        self.name = name
        self.country = country
        self.age = age


