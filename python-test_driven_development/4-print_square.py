#!/usr/bin/python3
'''
    create function that print a square with the character #
'''


def print_square(size):
    '''
        function print_square
    '''
    try:
        for i in range(size):
            print()
            for j in range(size):
               print("#", end="") 
    except:
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        if type(size) is float and size < 0:
            raise TypeError('size must be an integer')