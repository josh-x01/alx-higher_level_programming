#!/usr/bin/python3
"""Module 0-lookup.
Finding all attrubutes and methods of an object and store it in the list.
"""


def lookup(obj):
    """Return the list of attributes and method without the their values

    Args:
        - obj: the object where the attributes and method found
    """

    return getattr(obj)
