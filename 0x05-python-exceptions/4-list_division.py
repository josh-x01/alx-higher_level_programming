#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for num in range(list_length):
        try:
            res = my_list_1[num] / my_list_2[num]
        except ZeroDivisionError:
            print("division by 0")
            res = 0
        except IndexError:
            print("out of range")
            res = 0
        except TypeError:
            print("wrong type")
            res = 0
        finally:
            result += [res]
    return result
