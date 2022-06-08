#!/usr/bin/python3
def uniq_add(my_list=[]):
    copy_list = []
    for i in my_list:
        if i not in copy_list:
            copy_list.append(i)
    result = 0
    for i in copy_list:
        result = result + i
    return result
