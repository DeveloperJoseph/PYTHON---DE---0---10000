## FOR LOOPS ##
# A for loop is used for iterating over a sequence(that is
# either a list, a tuple, a dictionaru , a set, or a string).

#This is lees like the for keyword in other programming language,
#and works more like an iterator method as found in other
#object-orientated programming language.

#With the for loop we can execute a set of statements, once for
#each item in a list, tuple, set, etc.

#EXAMPLE: "Print each accesories in a accesories list"

#Declaramos nuestra variable 'accesories' como un listado
accesories = ["computer","pendrive","mouse","keyword"]
accesories.append("cd")#add item
accesories.append("headphone")#add item
x=0#variable inicializa en 0
j=0#variable inicializa en 0


#declarando mi variable 'cant' para almacenar la entrada de nuestro
#usuario y convertiendo el valor de tipo 'int', además declaro
#un 'ciclo for' el cual permite realizar un bucle con el valor
#ingresado previamente para ingresar los nombres de item a agregar en
#nuestro listado , por último una 'condicion if' donde evaluo el
#valor de 'j' si es mayor a nuestro valor ingresado por el
#usuario, si cumple esta condicion salimos automaticamente de nuestro
#'ciclo for'.
cant = int(input(">> Cantidad de accesorios para agregar: "))
for j in range(cant):
    item = input(">> Name item: ")
    accesories.append(item)
    if j > cant:
        break       
t = len(accesories)#obtener la longitud de nuestro listado

#En esta parte del programa declaramos un 'ciclo while' donde
#evaluamos 'x' que inicializa en 0 sea menor o igual que 't' que es 
#la longitud de nuestra lista, además inicializamos un 'ciclo for'
#el cual nos permite recorrer los valores de cada item de nuestro 'listado
#accesories', donde nuestra variable x suma 1 en cada recorrido de nuestro bucle,
#y por último imprime el valor de su posición y el valor del item del listado.
while x <= t:
    for a in accesories:
        x+=1
        print("Accesorio ",x,": ",a)
    break

def length(cadena):
    count = 0
    for i in cadena:
        count+=1
    return count

#entrada = input("Enter a phrase: ")
lista = [1,2,3,5,6,7,23,546]
print("Length of the phrase: ",length(lista))

