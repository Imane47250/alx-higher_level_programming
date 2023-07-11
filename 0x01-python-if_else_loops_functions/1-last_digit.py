#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    u = number % 10
    if u == 0:
        print(f"Last digit of {number :d} is 0 and is 0")
    elif u > 5:
        print(f"Last digit of {number :d} is", u, "and is greater than 5")
    elif u < 6:
        print(f"Last digit of {number} is", u, "and is less than 6 and not 0")
elif number < 0:
    u = -((-number) % 10)
    if u == 0:
        print(f"Last digit of {number :d} is 0 and is 0")
    elif u < 6:
        print(f"Last digit of {number} is", u, "and is less than 6 and not 0")
