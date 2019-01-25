## PYTHON ITERATORS ##
# - An iterator is an object that contains a countable number of values.
# - An iterator is an object that can be iterated upon, meaing that you can
#  traverse through all the values.
# - Technically, in Python, an iterator is an object which implements the iterator protocol,
#   which consist of the methods __iter__() and __next__().

# Iterator vs Iterable:
# - List, Tuples, Dictionaries , and sets are all iterable objects. They are iterable containers
#   which you can get an iterator from.
# - All these objects have a iter() method wich is used to get an iterator
#Example:
    # Return a iterator from a tuple, and print each value:
""""
my_tuple=('apple','banana','cherry','watermelon')
my_new_iterator = iter(my_tuple)#new iter
#loop for int the length range of my tuple created previusly
for x in range(len(my_tuple)):
    print(next(my_new_iterator))
"""
#Even string are iterable objects, and can return an iterator:
#Exampe:
   # - String are also iterable objects, containing a sequence of characters:
"""   
itered_fruit = iter(my_tuple[3])
for x in range(len(my_tuple[3])):
    print(next(itered_fruit))
"""
#Create an Iterator:
# - To create an object/class as an iterator you have to implement the methos __iter__() 
#   and __next__() to your objects.
# - All classes have a function called __init__(), which allows you do some initializing
#   when the object is being created.
# - The __iter__() methos acts similar, you can do operations(initializing etc.), but must
#   always return the iterator object itself.
# - The __next()__ method also allows you to do operations, and must return the next item
#   in the sequence.
#Example:
# Create an iterator that returns numbers, starting with 1, and each sequence will increase
# by onen (returning 1,2,3,4,5 etc.):
"""
class myNumbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x = self.a
        self.a +=1
        return x 

myClass = myNumbers()
myIter = iter(myClass)

count = int(input(">> Enter cant. of numbers for generar: "))
for i in range(count):
    print(next(myIter))
"""
#or
class myNumbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <=20:
            x = self.a
            self.a +=1
            return x
        else:
            raise StopIteration

myClass = myNumbers()

myIter = iter(myClass)
for x in myIter:
    print(x)
             