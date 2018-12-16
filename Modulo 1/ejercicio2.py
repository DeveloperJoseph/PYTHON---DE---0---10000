print("\n============================================================ ")
print(" =============   ENCHANTED FOREST STORE      ================ ")
print(" ================== @ Developer Joseph  ===================== ")
print(" ============================================================ ")


print("> Enter your name: ")
x = input()
print("> Enter your cant. of money: ")
money = input()
print("============================================================")
print(" Hello ",x,", Welcome to Python.")

myArrayList = ["Banana","Pineaple","Pear","Watermelon","Orange","Strawberry",
               "Grape","Cherry","Maca","Kiwi","Coconut","Black Grapes","Green Grapes"] 

print("============================================================")
print("Frutas en stock: ")

for name in myArrayList:
    print("#>",name)
print("============================================================")

print(">> Fruits your presupest:")
if int(money) >= 2.5 and int(money)<=20:
    for i in myArrayList:
        if i == "Banana":
            print("#>",i," , $2.50kg")
            continue
        elif i == "Pear":
            print("#>",i," , $4.50kg")
            continue
        elif i == "Orange":
            print("#>",i," , $3.50kg")
            continue
else:
    print(">> No tienes suficiente dinero...")
#elif int(money)>=21 and int(money)<=40:
#    for i ==


print("===============================")
print("Goodbye,"+x)
print("===============================")