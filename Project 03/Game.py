def add_item(inventory):
    """Asks the user for an item name and adds it to the inventory list."""
    item = input("Enter the name of the item to add: ")
    inventory.append(item)
    print(f"'{item}' was added to the inventory.")


def show_inventory(inventory):
    """Prints the contents of the inventory list to the user."""
    if not inventory:
        print("The inventory is empty.")
    else:
        print("Current inventory:")
        for index, item in enumerate(inventory, start=1):
            print(f"  {index}. {item}")


def remove_item(inventory):
    """Asks the user for an item name and removes it from the inventory, if found."""
    item = input("Enter the name of the item to remove: ")
    if item in inventory:
        inventory.remove(item)
        print(f"'{item}' was removed from the inventory.")
    else:
        print(f"'{item}' was not found in the inventory.")


def print_menu():
    """Prints the main menu options."""
    print("\n--- Main Menu ---")
    print("1. Add item")
    print("2. Show inventory")
    print("3. Remove item")
    print("4. Quit")


#main program
inventory = []

while True:
    print_menu()
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        add_item(inventory)
    elif choice == "2":
        show_inventory(inventory)
    elif choice == "3":
        remove_item(inventory)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")