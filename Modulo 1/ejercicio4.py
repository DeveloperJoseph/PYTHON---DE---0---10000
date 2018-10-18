
#ARRAY LISTS SIN CICLO FOR + SALIDA
the_list = ["love","sad","funny","crazy"]#My list of feelings 
print(">> The list is (without for): "+str(the_list))#salida de mi lista de array
print("## The item in position '0' of the list is (without for): "+the_list[0])
print("## The item in position '1' of the list is (without for): "+the_list[1])
print("## The item in position '2' of the list is (without for): "+the_list[2])
print("## The item in position '3' of the list is (without for): "+the_list[3])

#ARRAY LIST CON CICLO FOR + SALIDA
the_list2 = ["rabbit","cat","dog","parrot"]
print(">> The list number 2 is (with for): "+str(the_list2))
for animal in the_list2:
    print("## The animal secret is: "+animal)
    if "rabbit" in animal:
        print("## My favorite animal is rabbit and is in the list 2.")
print("The list number has "+str(len(the_list2))+" items.")


