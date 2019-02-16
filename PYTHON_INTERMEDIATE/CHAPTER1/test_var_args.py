##  *ARGS AND **KWARGS  ##

#Usage of *args and **kwargs #

# *ARGS: Are mostly used in function definitions.
# *args and **kwargs allow you to pass a variable number of arguments
# to a function. 

def test_var_args(first_args, *argv):
    print("> First argument input is (developer): ",first_args)
    for arg in argv:
        print("> Another args trough *argv are: ",arg)
    else:
        print("> Goodbye user.")
#test_var_args("Joseph","Rabbit","Cat","Dog","Elephant","tiger")


# **KWARGS: **kwargs allows you to pass keyworded variable 
#           length of arguments to a function.
# You should use **kwargs if you want  to handle named arguments 
# in a function. Here is an example to get you going with it.
# So you can see how we handled a keyworded arguments list in our
# function. This is just the basic of **kwargs and you can see how 
# useful it's. Now let's talk about  how you can use *args and **kwargs
# to call a function with a list or dictionary of arguments.  

def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("> {} and {} <".format(key,value))
#greet_me(myName="Joseph")

#  So you can see how we handled a keyworded argumenr list in
#  our function. This is just the basic of **kwargs and you 
#  can see how useful it's. Now let's talk about  how you can
#  use *args and **kwargs to call a function with a list or
#  dictionary of arguments.  

## USING *ARGS AND **KWARGS TO CALL A FUNCTION ##
# So here we will see how to call a function using *args and 
# **kwargs. Just consider that you have this little function.

def test_args_kwarg(arg1,arg2,arg3):
    print("arg1: ",arg1)
    print("arg2: ",arg2)
    print("arg3: ",arg3)

# Now you can use *args or **kwargs to pass arguments to this little function.
# Here's how to do it:
"""
# FIRST WITH *args
print("> Example *args:")
args = ("two",3,'six')
test_args_kwarg(*args)

# NOW WITH *kwargs
print("> Example **kwargs:")
kwargs = {"arg3":3,"arg2":"two","arg1":5}
test_args_kwarg(**kwargs)
"""

# ORDER OF USING *agrs **kwargs AND FORMAL ARGS:
# So if you want to use all three of these in functions 
# then the order is:

def some_function(fargs,*args,**kwargs):
        print("> Simple args: ",fargs)
        if len(args)> 0 or args !=None:
                for x in args:
                        print("> Values of *args: ",x)     
        if len(args)<=0 or args == None:
                print("> Null values in *args") 

        if len(kwargs)> 0 or kwargs !=None:
                for x in kwargs:
                        print("> Values of *kwargs: ",x)
        if len(kwargs)<=0 or kwargs==None:
                print("> Null values in *kwargs")               
#some_function("Hello")

