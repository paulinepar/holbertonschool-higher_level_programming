#!/usr/bin/python3
'''
    Write a function that creates an Object from a “JSON file”:
'''


import json
'''json import'''


def load_from_json_file(filename):
    '''function that create object from json'''
    with open(filename, 'r', encoding="UTF8") as f:
        return json.load(f)
