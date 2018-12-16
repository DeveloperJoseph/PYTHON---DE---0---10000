# PYTHON WHILE LOOPS #
print("\n # PYTHON WHILE LOOPS # ")
# Python has two primivite loop commands: (while, for)

# The while loop:
print("## The while loop...")
# Whith the 'while' loop we can execute a set of statements
# as long as  a condition is true.
# Example: "Print i as long as i is less than 6"
print("# Example: 'Print i as long as i is less than 6'")

i = 1
par=0
div_4=0
impar=0
div_3=0
while i <=5:
    if i % 2 ==0:
        par+=1
        if i % 4==0:
            div_4+=1
    else:
        if i % 3==0:
            div_3+=1
        impar+=1
    print(i)
    i+=1
print("> Count of par: "+str(par))
print("> Count of divisor 4: "+str(div_4))
print("> Count of impar: "+str(impar))
print("> Count of divisor 3: "+str(div_3))

x = 3
print("\n")
while x < 20:
    if x == 10:
        print("\n>exit....")
        break
    print("#> "+str(x))   
    x+=1