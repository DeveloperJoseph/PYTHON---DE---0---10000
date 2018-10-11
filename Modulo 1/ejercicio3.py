#ENTRADA DE DATOS   
a = "Joseph"

#Obtenga el carácter en la posición 1 (recuerde que el primer carácter tiene la posición 0):
print(a[0]+a[0]+a[0])
print(a[1]+a[1]+a[1])
print(a[2]+a[2]+a[2])
print(a[3]+a[3]+a[3])
print(a[4]+a[4]+a[4])
print(a[5]+a[5]+a[5])
print("==========")

b = "¡Whoami!"
print(b[1:7])#Subcadena Obtenga los caracteres de la posición 2 a la posición 5 (no incluidos)

#El método strip () elimina cualquier espacio en blanco desde el principio o el final:
c  = " HELLO, JOSEPH! "
print(c.strip())

#El método len () devuelve la longitud de una cadena:
d = "Joseph"
print("\nLa longitud de caracteres del nombre('Joseph') es: "+str(len(d)))

#El método lower () devuelve la cadena en minúsculas:
e = "WHOAMI"
print("\nReturn Mayúscula: "+e.lower())

#El método upper () devuelve la cadena en mayúsculas:
f = "conejo"
print("\nReturn Minúscula: "+f.upper())

#El método replace () reemplaza una cadena con otra cadena:
g = "YOSEPH"
print("\nNombre correcto: "+g.replace("Y","J")+" y no: "+g)

#El método split () divide la cadena en subcadenas si encuentra instancias del separador:
h = "JOSEPH * WHOAMI  * DEVELOPER"
print(" ")
print(h.split("*"))

#####################################################################

#Consulta de nombre y edad
print("\nWhat's your name?: ")
x = input()
print("Age?: ")
y = input()

print("\nHello, "+x+".")
print("Su edad es: "+y+".")