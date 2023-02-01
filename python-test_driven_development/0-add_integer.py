#!/usr/bin/python3
"""
    Function calculation
"""


def add_integer(a, b=98):
    """function addition"""
    try:
        sum = a + b
        return int((sum))
    except TypeError:
        if type(a) is not int:
            return 'a must be an integer'
        else:
            return 'b must be an integer'
