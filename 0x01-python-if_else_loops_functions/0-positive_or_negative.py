#!/usr/bin/python3
import random
number = random.randint(-10, 10)
a = int(input('Please enter an integer: '))
if a > 0:
    print(a, 'is positive')
elif a == 0:
    print(a, 'is zero')
else:
    print(a, 'is negative')
