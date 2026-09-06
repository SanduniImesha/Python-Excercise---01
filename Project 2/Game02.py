age = int(input("Enter your age: "))

if age < 12:
    print("You are a minor. The program will now close.")
else:
    name = input("What is your name? ")
    print(f"Welcome, {name}!")

    while True:
        print("\n--- Main Menu ---")
        print("Commands: kartta, reppu, taika, lopeta")
        command = input("> ")

        if command == "kartta":
            print("You open the map. You are standing at the crossroads.")
        elif command == "reppu":
            print("Your backpack contains: a torch, a rope, and 3 gold coins.")
        elif command == "taika":
            print("You cast a spell! Sparks fly from your fingertips.")
        elif command == "lopeta":
            print("Goodbye!")
            break
        else:
            print(f"Unknown command: {command}")