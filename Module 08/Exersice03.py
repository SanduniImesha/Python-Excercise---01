airports = {}

while True:
    print("\nWhat do you want to do?")
    print("  1 - Enter a new airport")
    print("  2 - Fetch airport information")
    print("  3 - Quit")
    choice = input("Choose an option (1-3): ")

    if choice == "1":
        icao_code = input("Enter the ICAO code: ")
        name = input("Enter the airport name: ")
        airports[icao_code] = name
        print(f"Airport '{name}' saved with code {icao_code}.")

    elif choice == "2":
        icao_code = input("Enter the ICAO code to look up: ")
        if icao_code in airports:
            print(f"{icao_code} -> {airports[icao_code]}")
        else:
            print(f"No airport found with code {icao_code}.")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice, please try again.")