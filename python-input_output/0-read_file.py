#!/usr/bin/python3
'''
    Write a function that reads a text file (UTF8) and prints it to stdout:
'''


def read_file(filename=""):
    '''function read_file'''
    with open(filename, encoding='UTF8') as f:
        print(f.read(), end="")
