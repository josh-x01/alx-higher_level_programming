#!/usr/bin/python3
class Square:

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.size is 0:
            print("")
        else:
            for q in range(self.position[1]):
                print("")

            for x in range(self.size):
                for t in range(self.size + self.position[0]):
                    if t < self.position[0]:
                        print(" ", end="")
                    else:
                        print("#", end="")
                print("")

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        elif int(size) >= 0:
            self.__size = size
        else:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        Error = TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise Error
        elif (isinstance(value[1], int) and isinstance(value[0], int))is True:
            if value[1] >= 0 and value[0] >= 0:
                self.__position = value
            else:
                raise Error
        else:
            raise Error

    def __str__(self):
        __list = ""
        if self.size <= 0:
            __list = ""
        else:
            for q in range(self.position[1]):
                __list += "\n"

            for x in range(self.size):
                for t in range(self.size + self.position[0]):
                    if t < self.position[0]:
                        __list += " "
                    else:
                        __list += "#"
                if (x != self.size - 1):
                    __list += "\n"
        return __list
