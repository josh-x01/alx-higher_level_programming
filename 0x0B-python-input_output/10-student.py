#!/usr/bin/python3
"""student class"""


class Student:
    """define student
    attr:
        - firstname
        - lastname
        - age
    """
    def __init__(self, first_name, last_name, age):
        """Initializes the class with the given arguments"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return the description"""
        my_dict = dict()
        if type(attrs) is list and all(type(x) is str for x in attrs):
            return self.__dict__.copy()
