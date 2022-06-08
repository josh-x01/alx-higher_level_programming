#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        new_key = ""
        tmp = 0
        for key, val in a_dictionary.items():
            if val > tmp:
                tmp = val
                new_key = key
        return new_key
