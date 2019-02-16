## GENERATORS ##

# First let's understand the iterators. According to
# Wikipedia, an iterator is an object that enables a 
# programmer to traverse a container, particularly lists. 
# However an iterator performs traversal and gives access
# to data elements in a container, but does not perform 
# iteration. You might be confuses so lets take it a bit slow. 
# There are three parts namely: ITERABLE, ITERATOR, ITERATION.

# All of these parts are linked to each other. We will
# discuss them one by one and later talk about generators.

# 3.1 ITERABLE: An iterable is any object in Python which has
#              an __iter__ or a  __getitem__ method defined which
#              returns an iterator or can take indexes(Both of these
#              dunder methods are fully explained in a previous chapter).
#              In short an iterable is any object which can provide us
#               with an iterator. So what is an iterator?

"""
def some_function():
    for i in range(15):
        yield i

for x in some_function():
    print(x)
"""

def fibonacci(n):
    a = b = 1 # 'a' and 'b' init with value 1 
    for i in range(n):#for loop
        yield a
        a, b = b , a + b#increment values de a with b and b with a + b

for value in fibonacci(10):#init function fibonacion with for loop
    print(value)#print get value