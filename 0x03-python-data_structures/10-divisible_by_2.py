#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    _bool = []
    for i in range(len(my_list)):
        if (my_list[i] % 2 == 0):
            _bool.append(True)
        else:
            _bool.append(False)
    return (_bool)
