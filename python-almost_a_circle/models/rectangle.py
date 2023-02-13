#!/usr/bin/python3
'''
    Write the class Rectangle that inherits from Base:
'''
Base = __import__('base.py').base


class Rectangle(Base):
    '''class Rectangle that inherits from base'''

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(self)
        self.id = id
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.x
    
    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.y

    @y.setter
    def y(self, value):
        self.__y = value

    @property
    def width(self):
        return self.width

    @width.setter
    def widht(self, value):
        self.__width = value

    @property
    def height(self):
        return self.height

    @height.setter
    def height(self, value):
        self.__height = value
