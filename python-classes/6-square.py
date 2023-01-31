#!/usr/bin/python3
"""Create an empty class."""


class Square():
    """class Square.
    """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    #getter of size
    def size(self):
        return self.__size

    @size.setter
    #setter of size
    def size(self, value):
        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size ** 2

    @property
    #getter of position
    def position(self):
        return self.__position

    @position.setter
    #setter of position
    def position(self, value):
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        if self.__size == 0:
            return print()
        for esp in range(self.__position[1]):
                print(end="\n" if self.__position[1] > 0 else "")
        for i in range(self.__size):
            for esp in range(self.__position[0]):
                print(end=" ")
            for j in range(self.__size):
                print("#", end="")
            print()
