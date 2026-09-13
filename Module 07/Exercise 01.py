import random


def roll_dice():
    """Returns a random dice roll between 1 and 6. No parameters."""
    return random.randint(1, 6)


# main program

result = roll_dice()
print(result)

while result != 6:
    result = roll_dice()
    print(result)

print("Rolled a 6! Done.")