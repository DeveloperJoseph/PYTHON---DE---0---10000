
# TUPLES EN PYTHON: #

#Una tupla es una colección que está ordenada e inmutable .
#En Python, las tuplas están escritas con corchetes.
print("## Iniciando tutorial............")
thisTuple = ("apple","banana","cherry")#new tuple  
print(">| Mi tuple  collection: "+str(thisTuple))#salida de mi tuple

# ACCEDER A LOS CAMPOS DE MI TUPLE #
print("## Accediendo con los indices de mi coleccion tuple...........")
print(">| El primer item de mi coleccion tuple es: "+str(thisTuple[0]))
print(">| El second item de mi coleccion tuple es: "+str(thisTuple[1]))
print(">| El tercer item de mi coleccion tuple es: "+str(thisTuple[2]))

# MODIFICAR LOS VALORES DE MI TUPLES - NO  ES POSIBLE #
#Una vez que se crea una tupla, no puede cambiar sus valores. Las tuplas son inmutables 

# Este bloque de codigo genera error:
#print("## Modificando los items de mi tuple...........")
#thisTuple[0]="orange"
#thisTuple[1]="pineapple"
#thisTuple[2]="watermelon"
#print("## Salida de mi nuevo collecion tuple...........")
#print(">| Mi nuevo tuple collection is: "+str(thisTuple)) 


## Bucle a traves de mi tuple collection ##
#Puede recorrer los elementos de la tupla utilizando un for bucle.

print("## Salida de mi tuple con un ciclo for......")
for item in thisTuple:
    print("Mi item es (ciclo for): "+str(item))
print("## Fin ciclo for......")


## COMPROBAR SI EXISTE  UN ITEM EN MI TUPLE ##
print("## Comprobando si existe mi fruta 'cherry' en mi collection.....")
if "cherry" in thisTuple:
    print(">| Yes, "+str(thisTuple[2])+" is in the fruits tuple")

## COMPROBAR LONGITUD DE TUPLE ##
print("## Calculando la longitud de mi collection.....")
print(">| La longitud de items de mi fruits tuple es: "+str(len(thisTuple)))


## Agregar articulos ##
#Una vez que se crea una tupla, no puede agregarle elementos. Las tuplas son inmutables .

#Este bloque de codigo genera error al agregar nuevo item

#thistuple = ("apple", "banana", "cherry")
#thistuple[3] = "orange" # This will raise an error
#print(thistuple)


## REMOVE ITEMS ##

#Nota: no puede eliminar elementos de una tupla.
#Las tuplas no se pueden cambiar , por lo que no puede eliminar elementos de ella, 
#pero puede eliminar la tupla por completo:

print("## Eliminado mi fruits tuple....")
del thisTuple
print(">| Fruits tuple eliminado....")


## La tupla () Constructor ##

#También es posible usar el constructor tuple () para hacer una tupla.  
print("## Creando un nuevo contructor tipo tuple")
mi_new_tuple = tuple(("rabbit","cat","dog"))
print(">| Salida de mi nuevo tuple constructor es: "+str(mi_new_tuple))

print("## Recorriendo items de mi constructor tuple con un ciclo for...")
for animal in mi_new_tuple:
    print(">| Item de constructor tuple: "+animal)

print("Mensaje aplicativo: See you later. Goodbye....")
print("### END END END END END END ###")



