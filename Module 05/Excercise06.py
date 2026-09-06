import random

N = int(input("How many random points do you want to generate? "))
n = 0
count = 0

while count < N:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 < 1:
        n += 1
    count += 1

pi_estimate = 4 * n / N
print(f"Approximation of pi after {N} points: {pi_estimate}")