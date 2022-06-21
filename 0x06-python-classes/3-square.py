#!/usr/bin/python3
""" Creates an empty class called Square
"""


class Square:
    """
    Class definition: Square

    Attributes:
    __size (int): square size private

    """
    def __init__(self, size=0):
        """
        Args:
            size: swuare size

        Raises:
            TypeError: if size is not type int
            ValueError: if size is negative
        """
        self.__size = size

        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size ** 2
