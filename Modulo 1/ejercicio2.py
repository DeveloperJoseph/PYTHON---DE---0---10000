print("\n============================================================ ")
print(" =============   ENCHANTED FOREST STORE      ================ ")
print(" ================== @ Developer Joseph  ===================== ")
print(" ============================================================ ")


print("> Enter your name: ")
x = input()
print("> Enter your cant. of money: ")
money = input()
print("> Enter the fruit you are looking for: ")
favorite_fruit = input()

print("============================================================")
print(" Hello ",x,", Welcome to Python.")

myArrayList = ["Banana","Pineaple","Pear","Watermelon","Orange","Strawberry",
               "Grape","Cherry","Maca","Kiwi","Coconut","Black Grapes","Green Grapes"] 

print("============================================================")
print("Frutas en stock: ")

if favorite_fruit in myArrayList:
    print(">> Your fruit is here to buy now...")
else:
    print(">> Your fruit isn't here , buy other...")
    
for name in myArrayList:
    print("#>",name)
print("============================================================")

print(">> Fruits your presupest (",money," dollars):")
if float(money) >= 2.5 and float(money)<5:
    for i in myArrayList:
        if i == "Banana":
            print("#>",i," - $2.50kg")
            continue
        elif i == "Orange":
            print("#>",i," - $3.50kg")
            continue
        elif i == "Pear":
            print("#>",i," - $4.50kg")
            continue
        elif i == "Grape":
            print("#>",i," - $4.99kg")
elif float(money) >= 5 and float(money)<=10:
     for i in myArrayList:
        if i == "Pineaple":
            print("#>",i," - $5.50kg")
            continue
        elif i == "Watermelon":
            print("#>",i," - $6.70kg")
            continue
        elif i == "Kiwi":
            print("#>",i," - $7.90kg")
            continue
        elif i == "Strawberry":
            print("#>",i," - $8.20kg")
            continue
        elif i == "Cherry":
            print("#>",i," - $8.50kg")
            continue
        elif i == "Coconut":
            print("#>",i," - $9.90kg")
            continue
elif float(money) > 10 and float(money)<=20:
    for i in myArrayList:
        if i ==  "Black Grapes":
            print("#>",i," - $15.50")
            continue
        elif i=="Green Grapes":
            print("#>",i," - $13.50")
            continue
        elif i=="Maca":
            print("#>",i," - $18.90")            
            continue
else:
    print(">> You don't have enough money to buy here....")


print("===============================")
print(">> Goodbye,"+x)
print("===============================")

