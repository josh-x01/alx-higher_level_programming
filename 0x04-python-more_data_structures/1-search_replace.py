#!/usr/bin/python3
def search_replace(my_list, search, replace):
    copy_list = my_list[:]
    copy_list = list(map(lambda x: x if x != search else replace, copy_list))
    return copy_list
