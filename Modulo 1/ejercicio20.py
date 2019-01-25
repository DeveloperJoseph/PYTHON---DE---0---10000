## PYTHON LAMBDA ##
#A lambda function is a small anonymus function.
#A lambda function can take any number of arguments.

#Syntax: 
    # lambda arguments: expression

#The expression is executed and the result is returned:
#Example 1:
    # - A lambda function that adds 10 to the number passed in
    #   as an argument, and print the result:
"""
value_entered = int(input(">> Enter a number: ")) 
add_value_entered = int(input(">> Enter a number for add the previus number: "))   
x = lambda value_entered : value_entered + add_value_entered
x = lambda value_entered, add_value_entered: value_entered*add_value_entered
x = lambda value_entered, add_value_entered: print(value_entered) if value_entered > add_value_entered else print(add_value_entered)
print(">> ",x(value_entered,add_value_entered)) 
"""

#Creating a function for combined with a lambda:
def myFunctionWithLambda(n):
    return lambda a: a * n

value_entered = int(input(">> Enter a number: "))
value_entered2 = int(input(">> Enter a number for add value: "))
value_lambda = myFunctionWithLambda(value_entered2)
print(value_lambda(value_entered))