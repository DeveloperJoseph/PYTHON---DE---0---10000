
################## ARRAY LIST( COUNT(), EXTEND(), INDEX(), COPY() ) #####################
list_frutas = ["apple", "banana", "cherry","orange","banana","cherry","cherry"]
count_bananas_in_list_frutas = list_frutas.count("banana")
count_apples_in_list_frutas = list_frutas.count("apple")
count_cherrys_in_list_frutas = list_frutas.count("cherry")
count_oranges_in_list_frutas = list_frutas.count("orange")

apple_position = list_frutas.index("apple")
banana_position = list_frutas.index("banana")
cherry_position = list_frutas.index("cherry")
orange_position = list_frutas.index("orange")


print(">> Mi lista de frutas: "+str(list_frutas))
print("## Calculando cantidad de cada fruta en lista..............")

print(">| Cantidad de "+str(list_frutas[0])+" en mi lista es: "+str(count_apples_in_list_frutas)+
    " ,su posicion en la lista es: "+str(apple_position))
print(">| Cantidad de "+str(list_frutas[1])+" en mi lista es: "+str(count_bananas_in_list_frutas)+
   " ,su posicion en la lista es: "+str(banana_position))
print(">| Cantidad de "+str(list_frutas[2])+" en mi lista es: "+str(count_cherrys_in_list_frutas)+
  " ,su posicion en la lista es: "+str(cherry_position))
print(">| Cantidad de "+str(list_frutas[3])+" en mi lista es: "+str(count_oranges_in_list_frutas)+
   ", su posicion en la lista es: "+str(orange_position))


list_numeros = [4,5,1,2,3]#new array list numbers
list_numeros.sort()#new array list numbers + metodo sort()

list_frutas.extend(list_numeros)

print(">> Mi nuevo array list (cadena, enteros): "+str(list_frutas))
print("## Calculando longitud de new array list: "+str(len(list_frutas)))






