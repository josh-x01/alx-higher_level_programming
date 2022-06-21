#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        self.__size = size

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != float and type(value) != int:
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def __lt__(self, other):
        return (self.__size < other.__size)

    def __le__(self, other):
        return (self.area() <= other.area())

    def __eq__(self, other):
        return (self.area() == other.area())

    def __ne__(self, other):
        return (self.area() != other.area())

    def __gt__(self, other):
        return (self.area() > other.area())

    def __ge__(self, other):
        return (self.area() >= other.area())
