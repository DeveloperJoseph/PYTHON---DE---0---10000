#EXERCISES PYTHON #
#1.- Definir una función max() que tome como argumento
#dos números y devuelva el mayor de ellos.
import datetime

now = datetime.datetime.now()
this_year = now.year

def  method_max_two(a,b):
    if a > b:
        return a
    elif b > a:
        return b

def method_min_two(a,b):
    if a < b:
        return a
    elif b < a:
        return b

def promedio_two(a,b):
    suma = float(a)+float(b)
    promedio = suma/2.0
    return promedio

print(">> FELIZ NAVIDAD ",this_year,"<<")
print("## FIRST EXERCISE ##")
print(">>Enter number one: ")
n1 = input()
print(">>Enter number two: ")
n2 = input()
print("#> Value 'max' is: ",method_max_two(n1,n2))
print("#> Value 'min' is: ",method_min_two(n1,n2))
print("#> Value 'promedio' is: ",promedio_two(n1,n2))
print("#> Sesion: ",now)

#2.-Definir una función max() que tomes tres números
#como argumentos y devuelva el mayor de ellos.
def promedio_three(x,y,z):
    suma = float(x) + float(y) + float(z)
    promedio = suma/3.0
    return promedio

def method_max_three(x,y,z):
    if x > y and x > z:
        return x
    elif y > x and y > z:
        return y
    elif z > x and z > y:
        return z

def method_min_three(x,y,z):
    if x < y and x < z:
        return x
    elif y < x and y < z:
        return y
    elif z < x and z < y:
        return z

now = datetime.datetime.now()
print("\n## SECOND EXERCISE ##")
print(">>Enter number one: ")
n1 = input()
print(">>Enter number two: ")
n2 = input()
print(">>Enter number three: ")
n3 = input()
print("#> Value 'max' is: ",method_max_three(n1,n2,n3))
print("#> Value 'min' is: ",method_min_three(n1,n2,n3))
print("#> Value 'promedio' is: ",promedio_three(n1,n2,n3))
print("#> Sesion: ",now)