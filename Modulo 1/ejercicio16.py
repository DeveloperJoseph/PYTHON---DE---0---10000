## FOR LOOPS 2 ##
"""
#Data Entry
print("\n===========================================================")
number = int(input(">>Enter a number for see multiplication of the number entered: "))
multiplicate_number = int(input(">>Enter a number for multiplicate: "))
print("===========================================================")

x = 0 #declare variable x with value 0

#In this loop while 


while x<=multiplicate_number:
    print("> ",number,' X ',x," = ", str(number*x))
    x+=1
    if x > multiplicate_number:
        break


for x in range(multiplicate_number+1):
    print("> ",number,' X ',x," = ", int(number*x))
    #if x >=multiplicate_number:
    #    break
    x+=1
"""

for i in range(100-1,200+2-2):
    print(">",i)
print("===========================================================")    
print(">> Goodbyee...")
print("===========================================================")