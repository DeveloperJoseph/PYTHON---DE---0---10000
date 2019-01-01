## FOR LOOPS 2 ##

#Data Entry
number = int(input(">>Enter a number for see multiplication of the number entered: "))
multiplicate_number = int(input(">>Enter a number for multiplicate: "))
x = 0

"""
while x<=multiplicate_number:
    print("> ",number,' X ',x," = ", str(number*x))
    x+=1
    if x > multiplicate_number:
        break
"""

for x in range(multiplicate_number+1):
    print("> ",number,' X ',x," = ", int(number*x))
    #if x >=multiplicate_number:
    #    break
    x+=1
    
print(">> Goodbyee...")
