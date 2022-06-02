#!/usr/bin/python3
letter = 97
while (letter < 123):
    if (letter == 101 or letter == 113):
        letter += 1
        continue
    print("{}".format(chr(letter)), end='')
    letter += 1
