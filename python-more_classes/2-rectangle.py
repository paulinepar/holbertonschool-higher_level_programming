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
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        p = 2*(self.__width + self.__height)
        if self.__width == 0 or self.__height == 0:
            perimeter = 0
        return p