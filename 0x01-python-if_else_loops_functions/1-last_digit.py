#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
absvalue = abs(number)
if number > 0:
    r = absvalue % 10
elif number < 0:
    r = - (absvalue % 10)
if abs(r) > 5:
    print(f"Last digit of {number :d} is", r, "and is greater than 5")
elif r == 0:
    print(f"Last digit of {number :d} is 0 and is 0")
elif 0 < abs(r) < 6:
    print(f"Last digit of {number :d} is", r, "and is less than 6 and not 0")
