#!/usr/bin/python3
"""Module 4-inherits_from.
The object must be instance of the super class"""


def inherits_from(obj, a_class):
    """is the object instance of inherited class

    Args:
        - obj: the object to check
        - a_class: the class of super or current

    Return: True is the object is instance of inherited class
    otherwise False
    """

    return isinstance(obj, a_class) and type(obj) != a_class
