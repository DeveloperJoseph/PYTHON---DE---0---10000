dictionary = {}
while True:
    print("--- APP BIRTHDAY ---")
    print(">>(1) Show birthdays")
    print(">>(2) Add to Birthday list")
    print(">>(3) Exit")
    choice = int(input("Enter the choice: "))
    if choice == 1:
        if(len(dictionary.keys()))==0:
            print("Nothing to show..")
        else:
            name = str(input("Enter name to look for birthday: "))
            birthday= dictionary.get(name,"Not data found")    
            print("> Birthday: ",birthday)
    elif choice ==2:
        name = str(input("# Enter name:"))
        date = str(input("# Enter birthdate: "))
        dictionary[name]=date
        print("#> Birthday Added")
    elif choice == 3:
        break