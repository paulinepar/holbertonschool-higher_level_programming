#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = number % 10
last_neg = number % (-10)
if number < 6 and number != 0:
    print(f"Last digit of {number} is {last_neg} and is less than 6 and not 0")
if number == 0:
    print(f"Last digit of {number} is {last} and is 0")
if number > 6:
    print(f"Last digit of {number} is {last} and is greater than 5")
