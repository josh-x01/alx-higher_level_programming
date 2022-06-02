#!/usr/bin/python3
for i in range(9):
    for j in range(1 + i, 10):
        if (i == 8):
            break
        print("{}{}".format(i, j), end=", ")
print("89")
