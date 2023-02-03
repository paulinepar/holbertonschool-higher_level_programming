#!/usr/bin/python3
"""
    class Rectangle
"""


class Rectangle():
    """
        An empty class Square.
    """
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def height(self):
        return self.__value

    @height.setter
    def height(self, value):

        self.__height = value
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")

    @property
    def width(self):
        return self.__value

    @width.setter
    def width(self, value):
        self.__width = value
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
