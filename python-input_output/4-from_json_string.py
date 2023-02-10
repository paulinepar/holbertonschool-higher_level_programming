#!/usr/bin/python3
'''
    Write a function that returns an object (Python data structure)
    represented by a JSON string:
'''


import json
'''json import'''


def from_json_string(my_str):
    '''function that return json data'''
    return json.loads(my_str)
