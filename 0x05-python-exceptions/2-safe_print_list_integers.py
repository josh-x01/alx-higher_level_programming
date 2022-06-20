#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    num = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            num += 1
        except ValueError:
            pass
        except IndexError:
            raise
        except TypeError:
            pass
    print("")
    return num
