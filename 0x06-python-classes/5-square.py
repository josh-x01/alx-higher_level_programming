#!/usr/bin/python3
""" Creates an empty class called Square
"""


class Square:

    def __init__(self, size=0):
        self.__size = size

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for num in range(self.__size):
                for num in range(self.__size):
                    print("#", end="")
                print("")

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
