#!/usr/bin/python3
import random
number = random.randint(-10, 10)
a = int(input("Please enter an integer: "))
if a > 0:
    print("is positive")
elif a == 0:
    print("is zero")
else:
    print("is negative")
