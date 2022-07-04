#!/usr/bin/python3
"""
Module 1-my_list.py.
print the inherited list in a sorted way.
"""


class MyList(list):
    """This class inherits from list."""

    def print_sorted(self):
        """sort the list and print it."""
        sorted_list = self[:]
        sorted_list.sort()
        print("{}".format(sorted_list))
