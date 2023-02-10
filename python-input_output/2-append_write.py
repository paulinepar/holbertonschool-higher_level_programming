#!/usr/bin/python3
'''
    Write a function that appends a string at the end of a text file (UTF8)
    and returns the number of characters added:
'''


def append_write(filename="", text=""):
    '''function that append a string'''
    with open(filename, 'a+', encoding='UTF8') as f:
        f.write(text)
        return len(text)
