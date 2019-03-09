## Map & Filter ##

#These are two functions which facilitate a functional approach to programming.
#We will discuss them one by one and understand their use cases.

# 4.1 Map: Map applies a function to all the items in an input_list.Here is the
#          blueprint:  map(funtion_to_apply, list_of_inputs)

#Most of the items we want to pass all the list elements to a function one by 
#one and then collect the output. For instance.
"""
items = [1,2,3,4,5]
squared = []    
for x in items:
    squared.append(x**2)#square
print(squared)
"""
items = [10,20,30,40,50,60,70,80,90,100]
squared = list(map(lambda x: x**2,items))
print(squared)