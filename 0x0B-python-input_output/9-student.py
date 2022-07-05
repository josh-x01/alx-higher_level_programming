#!/usr/bin/python3
"""student class"""


class Student:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def to_json(self):
        return self.__dict__
