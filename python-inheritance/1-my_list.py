#!/usr/bin/python3
'''
    Write a class MyList that inherits from list
'''

class MyList(list):
    def print_sorted(self):
        '''function print_sorted'''
        print(sorted(self))
