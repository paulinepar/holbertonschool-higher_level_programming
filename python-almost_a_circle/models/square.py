#!/usr/bin/python3
'''create class square that inherits from rectangle'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''class Square'''
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        return ('[Square] ({}) {}/{} - {}'.format
                (self.id, self.x, self.y, self.size))

    @property
    def size(self):
        return self.height

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''function args'''
        if len(args) > 0:
            for arg in range(len(args)):
                if args:
                    self.id = args[0]
                if arg > 0:
                    self.size = args[1]
                if arg > 1:
                    self.x = args[2]
                if arg > 2:
                    self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        '''create dict'''
        dict = {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
        return dict
