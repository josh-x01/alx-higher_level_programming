#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    all_set = []
    for i in set_1:
        all_set.append(i)
    for j in set_2:
        if j in all_set:
            all_set.remove(j)
        else:
            all_set.append(j)
    return all_set
