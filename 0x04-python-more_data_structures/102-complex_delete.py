#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    delete = []
    for key, val in a_dictionary.items():
        if val == value:
            delete.append(key)
            continue
    for i in delete:
        del a_dictionary[i]
    return a_dictionary
