while True:
    print("1. Pizza")
    print("2. Burger")
    print("3. Pasta")
    print("4. Exit")
    
    choice = input("Apna option chunein (1-4): ")
    
    if choice == "1":
        print("Aapne Pizza select kiya hai!")
    elif choice == "2":
        print("Aapne Burger select kiya hai!")
    elif choice == "3":
        print("Aapne Pasta select kiya hai!")
    elif choice == "4":
        print("Exiting... Thank you!")
        break  # Loop ko turant rok dega
    else:
        print("Invalid choice! Please try again.")