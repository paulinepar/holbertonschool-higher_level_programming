#!/usr/bin/python3
'''Write the class Rectangle that inherits from Base:'''
from models.base import Base


class Rectangle(Base):
    '''class Rectangle that inherits from base'''

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")

    def area(self):
        '''function area of rectangle'''
        return self.__height * self.__width

    def display(self):
        '''funtion print hashtag'''
        if self.__width == 0 or self.__height == 0:
            return print()
        else:
            for esp in range(self.__y):
                print()
            for i in range(self.__height):
                for esp in range(self.__x):
                    print(end=" ")
                for j in range(self.__width):
                    print("#", end="")
                print()

    def __str__(self):
        '''function update class rectangle'''
        return ('[Rectangle]({}) {}/{} - {}/{}'.format
                (self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        '''function args'''
        if len(args) > 0:
            for arg in range(len(args)):
                if args:
                    self.id = args[0]
                if arg > 0:
                    self.width = args[1]
                if arg > 1:
                    self.height = args[2]
                if arg > 2:
                    self.x = args[3]
                if arg > 3:
                    self.y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
