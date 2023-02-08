#!/usr/bin/python3
'''
    Write a class BaseGeometry (based on 5-base_geometry.py)
'''

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Class Rectangle'''
    def __init__(self, width, height):
        self.__width = width
        self.__heigth = height
