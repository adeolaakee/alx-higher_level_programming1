#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

# To get the last digit of a num you you'll use modulus
test = number % 10

# To print the last digit of negative number
if number < 0:
    test = -number % 10

if test > 5:
    print(f"Last digit of {number:d} is {test:d} and is greater than 5")
elif test == 0:
    print(f"Last digit of {number:d} is {test:d} and is 0")
elif (test < 6) and (test != 0):
    print(f"Last digit of {number:d} is {test:d} and is less than 6 and not 0")
