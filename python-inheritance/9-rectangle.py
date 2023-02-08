#!/usr/bin/python3
'''
    Write a class BaseGeometry (based on 5-base_geometry.py)
'''

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Class Rectangle'''
    def __init__(self, width, height):
        self.__height = height
        self.__width = width
        self.__height == BaseGeometry.integer_validator(self, 'height', self.__height)
        self.__width == BaseGeometry.integer_validator(self, 'width', self.__width)

    def area(self):
        return self.__height * self.__width
        
    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
