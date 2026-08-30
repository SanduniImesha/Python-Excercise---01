import random

# 3-digit code: each digit between 0 and 9
digit1 = random.randint(0, 9)
digit2 = random.randint(0, 9)
digit3 = random.randint(0, 9)
print(f"3-digit code: {digit1}{digit2}{digit3}")

# 4-digit code: each digit between 1 and 6
digit1 = random.randint(1, 6)
digit2 = random.randint(1, 6)
digit3 = random.randint(1, 6)
digit4 = random.randint(1, 6)
print(f"4-digit code: {digit1}{digit2}{digit3}{digit4}")