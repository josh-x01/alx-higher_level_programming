#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
non_negative = number
if (non_negative < 0):
    non_negative = -non_negative
    lastDigit = non_negative % 10
    lastDigit = -lastDigit
else:
    lastDigit = non_negative % 10
message = f"Last digit of {number:d} is {lastDigit:d} and is "
if (lastDigit > 5):
    print(message + "greater than 5")
elif (lastDigit == 0):
    print(message + "0")
else:
    print(message + "less than 6 and not 0")
