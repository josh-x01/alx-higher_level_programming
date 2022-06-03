#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy_list = []
    for i in range(len(my_list)):
        copy_list.append(my_list[i])
    if (idx < 0):
        return (copy_list)
    elif (idx > (len(my_list) - 1)):
        return (copy_list)
    else:
        copy_list[idx] = element
        return (copy_list)
