shopping_list = []

while True:
    print("\nShopping List Manager")
    print("1. Add item")
    print("2. Remove item")
    print("3. Show list")
    print("4. Check item")

    choice = input("Choice: ")

    if choice == "1":
        item = input("Enter item: ")
        shopping_list.append(item)
        print(f"Added '{item}' to the list!")

    elif choice == "2":
        item = input("Enter item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"Removed '{item}' from the list!")
        else:
            print(f"'{item}' not found in the list.")

    elif choice == "3":
        if not shopping_list:
            print("Your shopping list is empty.")
        else:
            print("\nYour Shopping List:")
            i = 1
            for item in shopping_list:
                print(f"{i}. {item}")
                i += 1

    elif choice == "4":
        item = input("Enter item to check: ")
        if item in shopping_list:
            print(f"Yes, '{item}' is in your shopping list.")
        else:
            print(f"No, '{item}' is not in your shopping list.")

    else:
        print("Invalid choice. Please enter 1 to 4.")

