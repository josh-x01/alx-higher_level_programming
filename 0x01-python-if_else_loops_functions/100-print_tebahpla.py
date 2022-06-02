#!/usr/bin/python3
for i in reversed(range(97, 123)):
    if (i % 2 != 0):
        i -= 32
    print("{}".format(chr(i)), end='')
