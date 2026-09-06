import random

target = random.randint(1, 10)

while True:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess > target:
        print("Too high")
    elif guess < target:
        print("Too low")
    else:
        print("Correct")
        break