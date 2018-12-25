# PYTHON WHILE LOOPS #
print("\n===================================")
print("# PYTHON WHILE LOOPS # ")
# Python has two primivite loop commands: (while, for)

# The while loop:
print("## The while loop...")
# Whith the 'while' loop we can execute a set of statements
# as long as  a condition is true.
# Example: "Print i as long as i is less than 6"

print(">> Enter your favorite  number min. : ")
favorite_number_min = input()
print(">> Enter your favorite number max. :")
favorite_number_max = input()

min = int(favorite_number_min)
max = int(favorite_number_max)
k = min
impar=0
par=0
#div_2=0
#div_3=0
#div_4=0
div_5=0
#div_6=0
#div_7=0
#div_8=0
#div_9=0
#div_10=0
#div_11=0
div_12=0
print("\n")
print("===================================")
print("|       - NUMBERS GENERATED -     |")
print("===================================")
while min <= max:
    if min % 2 ==0:
        par+=1
        #div_2+=1
    elif min % 2 !=0:
       impar+=1 
   
    while k <= max:
        if k % 5 ==0:
            div_5+=1
        elif k % 12 ==0:
            div_12+=1    
        k+=1      
    print("|",min,"                              |")#print numbers
    min+=1

print("===================================")
print("> Count of par: "+str(par))
print("> Count of impar: "+str(impar))
print("> Count of divisor 5: "+str(div_5))
print("> Count of divisor 12: "+str(div_12))
print("===================================")


print("\n>> Enter your favorite  number two: ")
favorite_number2 = input()

w=0
while w <= int(favorite_number2):
    w+=1 
    print(w)
    if w == 2:
        print("My Favorite number is: ",w)
        continue
    elif w == 5:
        print("My not favorite  number is: ",w)
        continue
    elif w ==3:
        print("My hater number: ",w)
        continue
    
    if w >=int(favorite_number2):        
        break    

