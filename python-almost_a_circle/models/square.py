#!/usr/bin/python3
'''create class square that inherits from rectangle'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''class Square'''
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size
        
    def __str__(self):
        return ('[Square] ({}) {}/{} - {}'.format(self.id, self.x, self.y, self.size))
