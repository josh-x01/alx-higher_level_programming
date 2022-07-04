#!/usr/bin/python3
"""Module 3-is_kind_of_class.
find object instance of a class.
"""


def is_kind_of_class(obj, a_class):
    """check an object is instance or inherited class instance of a class.

    Agrs:
        - obj: object to check
        - a_class: the main class to check

    Return: True is the object is instance or inherited from the class.
    """

    return isinstance(obj, a_class)
