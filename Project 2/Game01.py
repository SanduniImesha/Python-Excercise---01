age = int(input("Enter your age: "))

if age < 12:
    print("You are a minor. The program will now close.")
else:
    name = input("What is your name? ")
    print(f"Welcome, {name}!")

    while True:
        print("\n--- Main Menu ---")
        print("Enter a command (type 'lopeta' to quit):")
        command = input("> ")

        if command == "lopeta":
            print("Goodbye!")
            break
        else:
            print(f"Unknown command: {command}")