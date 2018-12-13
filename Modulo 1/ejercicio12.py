#PYTHON CONDITIONS AND IF STATEMENTS
#Supports the usual logical conditiions from mathematics:
# Equals: a==b
# Not Equals: a!=b
# Less than: a<b
# Less than or equal to: a<=b
# Greater than: a>b
# Greater than or equal to: a>=b
#These conditios can be used in several ways, mos commonly in "if statements" and loops,
#An "if statements" is written by using the if keyword.

print("\n#>Loading 'PYTHON CONDITIONS AND IF STATEMENTS', please wait.......")


# IF #
#In  this example, we use twi variables, a and b, wich are used as part of the if
#statement to test whetter b is greater than a. As a is 50, and b is 100, we know that
#100 is greater than 50, and so we print to screen that "b" is greater than "a".
print("\n#>Loading 'IF STATEMENT'.....")
print(">> First example if statement: ")
a = 50
b = 100
if b > a:
    print("> Reply: B is greater tan A")

# ELIF #
#The elif keyword is pythons way of saying 'if the previous condition were not true, then try 
#this condition'.
print("\n#>Loading 'ELIF STATEMENT'.....")
#In this examplea is equal to b, so the first codition is not true, but the elif condition is true,
#so we print to screen that "B AND A, ARE EQUALS".
print(">> Second example elif statement: ")
a = 33
b = 33
if b > a:
    print("> Reply: B is greater than A")
elif b == a:
    print("> Reply: B and A are equal")

# ELSE #
#The else keyword catches anything which isn't caught by the preceding conditions.
print("\n#>Loading 'ELSE STATEMENT'.....")
#In this example a is greater to b, so the first condition is not true, 
#also the elif condition is not true, so we go to the else condition 
#to screen that " A is greater than b".  
print(">> Third example else statement: ")
a = 200
b = 33
if b > a:
    print("> Reply: B is greater that A.")
elif a==b:
    print("> Reply: A and B are equals.")
else:
    print("> Reply: A is greater than B.")

#you can also have an else without the elif:
print("\n>> You can also have an else without the elif: ")
if b > a:
    print("> Reply: B is greater that A.")
else:
    print("> Reply: B is not greater that A.")

# SHORT HAND IF #
#If you have only one statement to execute, you can put it on the same line 
# as the if statements.
print("\n#>Loading SHORT HAND IF.....")
print(">> Fourth example short if: ")
if a > b: print("> A is greater than B por : "+str(a-b)+" puntos.")

# SHORT HAND IF...ELSE
# If you have only statement to execute, one for if, and one for else, you
# can put it alll on the same line:
print("\n#>Loading SHORT HAND IF..ELSE...")
print(">> Fourth example short if-else: ")
print("> A greater") if a > b else print("> B greater")
#You can also have multiple else statemet on the same line:
print(">> Fifth example multiple else on the same line: ")
a = 69
b = 69
print("> A greated") if a > b else print("> A and B are equals") if a ==b else print("> B greated")

# AND KEYWORD LOGICAL #
# The and keyword is a logical operator, and is used to combine conditional statements:
print("\n#>Loading AND keyword...")
print(">> Sixth example AND keyword: ")
a = 100
b = 50
c = 200
if a>b and c>a:
     print(">Both conditions are True")

print("\n#>Loading OR keyword...")
print(">> Seventh example OR keyword: ")
if a > b or a > c:
    print("At least one of the condition are true")

print("\n Thank you for attention...")
