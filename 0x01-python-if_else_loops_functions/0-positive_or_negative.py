#!/usr/bin/python3
import random
number = random.randint(-10, 10)
i = 0
if i > number:
    print(f"{number:d} is negative")
elif i < number:
    print(f"{number:d} is positive")
else:
    print(f"{number:d} is zero")
