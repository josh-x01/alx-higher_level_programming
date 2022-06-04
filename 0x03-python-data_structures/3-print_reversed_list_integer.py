#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    for i in range(len(my_list)):
        if (i == (len(my_list) - 1)):
                print("{}".format(my_list[i]), end="")
        else:
            print("{:d}".format(my_list[i]))
