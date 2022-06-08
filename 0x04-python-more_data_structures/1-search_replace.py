#!/usr/bin/python3
def search_replace(my_list, search, replace):
    copy_list = my_list[:]
    for i in copy_list:
        if i == search:
            i = replace
    return copy_list
