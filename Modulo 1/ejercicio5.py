#ARRAY LIST - AGREGAR ITEMS
                #0         1      2       3
list_things = ["table","book","chair",'xxxx']
list_things.append("desk")#add un nuevo item a la ultima posicion
print(">> Salida 1 de mi array: "+str(list_things))#salida de mi array
print("---> Modificicando el item en posición 3....")#salida mensaje help
list_things[3] = "pencil"#modificicando el item position 3

print(">> Salida 2 de mi array: "+str(list_things))#salida de mi array
print("---> Agregando un item en la posición 5....")#salida mensaje help
list_things.append("yyyy")

print(">> Salida 3 de mi array: "+str(list_things))#salida de mi array
print("---> Remove un item en la posición 5....")#salida mensaje help
list_things.pop()

print(">> Salida 4 de mi array: "+str(list_things))#salida de mi array
print("---> Remove un item en la posición 3....")#salida mensaje help
list_things.remove(list_things[3])

print(">> Salida 5 de mi array: "+str(list_things))#salida de mi array
copia_list_things = list_things.copy()#copiando array en nueva variable
list_things.clear()#limpiando items de nuestro array

print(">> Salida 6 de mi array: "+str(list_things)+" / 'ESTA VACIO'")#salida de mi array

print("*** EL BACKUP DE MI LISTA : "+str(copia_list_things)+" ****")#salida de nuestro nuevo array(copia)

print("Fin.........................................................!!!")




