import random

number_of_dice = int(input("How many dice do you want to roll? "))
total = 0

for _ in range(number_of_dice):
	roll = random.randint(1, 6)
	total += roll

print(f"Sum of all dice: {total}")
