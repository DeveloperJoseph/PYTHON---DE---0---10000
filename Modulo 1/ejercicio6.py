
# ARRAY LIST REVERSE AND SORT 
new_array_list_names = ["ConeS","Joseph","Daniel","Smith","Whoami","Ely"]
print("Your name")#Entrada de usuario
name = input()#Capturade entrada

print(">> Hello, "+name+", el nuevo array list de nombres: "+str(new_array_list_names))#salida 1

print("### Ordenando nuestro array list de manera alfabetica.......")#salida 2
new_array_list_names.sort()#Ordenando con el metodo sort 
print("-> ARRAY LIST DE NOMBRES ORDENADO (método sort): "+str(new_array_list_names))#salida 3

print("### Ordenando de manera reversa nuestro array list.......")#salida 4
new_array_list_names.reverse()#Ordenando de manera reversa 
print("-> ARRAY LIST DE NOMBRES ORDENADO (método reverse): "+str(new_array_list_names))#salida 5

print("#-> La cantidad de items de nuestro array es: "+str(len(new_array_list_names)))#metodo len() + salida 6
print("$$$$ FIN FIN FIN FIN FIN $$$$")

