#!/usr/bin/python3
'''Write the class Rectangle that inherits from Base:'''
from models.base import Base


class Rectangle(Base):
    '''class Rectangle that inherits from base'''

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__id = id
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value
        if type(value) is not int:
            raise TypeError(f"{self.__x} must be an integer")
        elif value < 0:
            raise ValueError(f"{self.__x} must be >= 0")


    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
        if type(value) is not int:
            raise TypeError(f"{self.__y} must be an integer")
        elif value < 0:
            raise ValueError(f"{self.__y} must be >= 0")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value
        if type(value) is not int:
            raise TypeError(f"{self.__width} must be an integer")
        elif value < 0:
            raise ValueError(f"{self.__width} must be > 0")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value
        if type(value) is not int:
            raise TypeError(f"{self.__height} must be an integer")
        elif value < 0:
            raise ValueError(f"{self.__height} must be > 0")
