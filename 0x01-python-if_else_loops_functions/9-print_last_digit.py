#!/usr/bin/python3
def print_last_digit(number):
    non_negative = number
    if (non_negative < 0):
        non_negative = -non_negative
        lastDigit = non_negative % 10
    else:
        lastDigit = non_negative % 10
    print("{}".format(lastDigit), end='')
    return lastDigit
