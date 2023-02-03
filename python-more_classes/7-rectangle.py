#!/usr/bin/python3
"""
    class Rectangle
"""


class Rectangle():
    """
        An empty class Square.
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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
        p = (self.__width * 2) + (self.__height * 2)
        if self.__width == 0 or self.__height == 0:
            return 0
        return p

    def __str__(self):
        hashtag = ""
        if self.__height == 0 or self.__width == 0:
            return ""
        for i in range(self.__height):
            for j in range(self.__width):
                hashtag += '#'
            if i + 1 < self.__height:
                hashtag += '\n'
        return hashtag

    def __repr__(self):
        repre = 'Rectangle(' + str(self.width) + ', ' + str(self.height) + ')'
        return repre

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1