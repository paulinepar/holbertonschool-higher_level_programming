#!/usr/bin/python3
'''
    Write a function that writes an Object to a text file,
    using a JSON representation:
'''

import json
'''json import'''


def save_to_json_file(my_obj, filename):
    '''function write object, using json'''
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
