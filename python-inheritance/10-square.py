#!/usr/bin/python3
'''
    Write a class Square that inherits from Rectangle (9-rectangle.py):
'''

BaseGeometry = __import__('7-base_geometry').BaseGeometry

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    '''class Square'''
    def __init__(self, size):
        self.__size = size
        super().integer_validator('size', size)

    def area(self):
        return self.__size * self.__size