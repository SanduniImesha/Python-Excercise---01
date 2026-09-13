import random


def roll_dice(sides):
    """Returns a random dice roll between 1 and 'sides'."""
    return random.randint(1, sides)


# --- main program ---
max_sides = int(input("Enter the number of sides on the dice: "))

result = roll_dice(max_sides)
print(result)

while result != max_sides:
    result = roll_dice(max_sides)
    print(result)

print(f"Rolled the maximum ({max_sides})! Done.")