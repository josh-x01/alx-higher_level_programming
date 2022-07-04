#!/usr/bin/python3
"""Module 2-is_same_class.
checking an object is instance of a class or not."""


def is_same_class(obj, a_class):
    """Return: True if obj os instamce of a_class, else False.
    
    Args:
        - obj: the object to check
        - a_class: the class where the object belong
    """
    
    return True if type(obj) is a_class else False
