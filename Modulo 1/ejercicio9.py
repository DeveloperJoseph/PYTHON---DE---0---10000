
## PYTHON SETS ##

# SET: A set is a collection which is unordered and unindexed.
# In Python sets are written with curly brackets { }

my_set = {"Banana","Cherry","Apple","Orange","Watermelon"}
print("Mi nuevo set en python: "+str(my_set))



## Cambiar Artículos ##
# Una vez que se crea un conjunto, no puede cambiar sus elementos,
# pero puede agregar nuevos elementos.


## Agregar articulos ##

# Para agregar un elemento a un conjunto use el add() método.
# Para agregar más de un elemento a un conjunto use el update() método.
print("## Agregando nuevos item a mi python set...")

#add()
my_set.add("pear")
my_set.add("grapes")

#update()
my_set.update(["Plum","Tangerine","Mango"])


## Obtener la longitud de un conjunto ##
print("## Calculando cantidad de items contiene nuestro set....")
#Para determinar cuántos elementos tiene un conjunto, use el len()método.
print(">| Cantidad de items: "+str(len(my_set)))

## Access Items ##
# You cannot access items in a set by referring to an index, since
# sets are unordered the items has no index.

# But you can loop through the set items using a for loop, or ask if
# a specified value is present in a set, by using the in keyword.
print("## Iniciando ciclo for en mi python set.....")
y = 1
for x in my_set:
    print(">| Mi "+str(y)+ " item es: "+x)
    if "Orange" in x:
        print("- My favorite fruit is: "+x)
    if "Apple" in x:
        print("- "+x+" is not my favorite fruit.")
    y +=1
print("## FIN FOR LOOP......")    


## Remover el artículo ##
#Para eliminar un elemento de un conjunto, utilice remove() o el método discard()  .

#remove()
print("## Eliminando mi item 'pear' ( metodo remove() )......")
#Nota: Si el elemento a eliminar no existe, se remove()generará un error.
my_set.remove("pear")

#discard()
print("## Eliminando mi item 'Banana' ( metodo remove() )......")
#Nota: Si el elemento a eliminar no existe, NOdiscard() generará un error.
my_set.discard("Banana")

## POP() - ELIMINAR ##
#También puede utilizar el pop() método, para eliminar un elemento, 
# pero este método eliminará el último elemento. Recuerde que los 
# conjuntos no están ordenados, por lo que no sabrá qué elemento se elimina.
# El valor de retorno del pop()método es el elemento eliminado.
# Nota: los conjuntos no están ordenados , por lo que al usar el pop()método, 
# no sabrá qué elemento se elimina.
print("## Eliminando un item alternativo de un python set con el metodo pop()...")
print(">| El item eliminado es: "+str(my_set.pop()))

## CICLO FOR 2 ##
print("## Nueva salida de  mi set fruits....")
a = 1
for z in my_set:
    print(">- Mi "+str(a)+" item is: "+z)
    a+=1
print("## Fin for loop 2........")

## METODO CLEAR ##
print("## Iniciando método clear a nuestro python set 'my_set'...")
# El clear() método vacía el conjunto:
my_set.clear()
print(">| Salida de nuestro set vacio con el método 'clear': "+str(my_set))
print(">| Cantidad de item de nuestro python set: "+str(len(my_set)))

## METODO DEL ##
# La palabra clave del eliminará el conjunto por completo:

# BLOQUE DE CODIGO COMENTADO GENERA ERROR AL ELIMINAR POR
# COMPLETO NUESTRO SET CON EL METODO SET()
   #  del thisset
   #  print(thisset)


## CONSTRUCTOR SET EN PYTHON ##
#También es posible usar el constructor set () para hacer un conjunto.
print("## Creando un constructor set en python.....")

new_set = set(("Dog","Cat","Parrot","Rabbit")) #constructor
print(">| Mi nuevo constructor set: "+str(new_set))

# CICLO FOR 

for animal in new_set:
    print("Mi animal es: "+animal)
print("## FIN CICLO FOR 3................")







    

