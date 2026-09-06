numbers = []

while True:
    entry = input("Enter a number (empty to quit): ")
    if entry == "":
        break
    numbers.append(float(entry))

numbers.sort(reverse=True)

print("Five greatest numbers:")
for value in numbers[:5]:
    print(value)