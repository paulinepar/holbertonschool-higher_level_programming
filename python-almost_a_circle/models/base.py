#!/usr/bin/python3
'''
    Write the first class Base:
'''


class Base():
    '''class'''

    __nb_objects = 0

    def __init__(self, id=None):
        self.id = id
        Base.__nb_objects += 1
        