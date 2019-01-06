#importing libraries requeried
from random import randint
from datetime import datetime


print("\n")
#Input of value
number = int(input(">> Enter un int number(generated random integer: "))

y = 0#value intialize with 0
while y<number:
    print(randint(0,number))#print random value
    if y > number:#condition if break
        break
    y+=1# 'y' increases its value +1


#for x in range(randint(0,number)):
#    print(">",x)


"""
value_entered = input(">> Enter a variable: ")
number_entered = int(input(">>Generated random integer: "))
new_list = [value_entered]*number_entered
print(new_list)
"""
print(">> Your Session: ",datetime.now())