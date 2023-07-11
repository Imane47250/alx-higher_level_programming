#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
final_number = abs(number)
r = final_number % 10
if r > 5:
    print(f"Last digit of {number :d} is", r, "and is greater than 5")
elif r == 0:
    print(f"Last digit of {number :d} is 0 and is 0")
elif 0 < number % 10 < 6:
    print(f"Last digit of {number :d} is", r, "and is less than 6 and not 0")
