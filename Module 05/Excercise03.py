smallest = None
largest = None

while True:
    entry = input("Enter a number (empty to quit): ")
    if entry == "":
        break
    number = float(entry)
    if smallest is None or number < smallest:
        smallest = number
    if largest is None or number > largest:
        largest = number

if smallest is None:
    print("No numbers were entered.")
else:
    print(f"Smallest: {smallest}")
    print(f"Largest: {largest}")