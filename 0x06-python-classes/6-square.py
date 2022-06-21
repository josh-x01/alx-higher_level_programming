#!/usr/bin/python3
class Square:

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        Error = TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise Error
        elif type(value[0]) == int and type(value[1]) == int:
            if value[0] < 0 or value[1] < 0:
                raise Error
            else:
                self.__position = value
        else:
            raise Error

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            print("\n" * self.__position[1], end="")
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
