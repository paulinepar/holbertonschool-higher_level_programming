#!/usr/bin/python3
"""
    Function calculation
"""


def add_integer(a, b=98):
    """function addition"""
    if a is float:
        a = int()
    if b is float:
        b = int()
    if a is not int or float:
        raise TypeError("a must be an integer")
    if b is not int or float:
        raise TypeError("b must be an integer")
    return a + b
