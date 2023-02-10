#!/usr/bin/python3
'''
    Write a script that adds all arguments to a Python list
    and then save them to a file:
'''


import sys
import json
'''json import'''
save_to_json_file = __import__('5-save_to_json_file.py').save_to_json_file

load_from_json_file = __import__('6-load_from_json_file.py').load_from_json_file

list = []
try:
    save_to_json_file(load_from_json_file("add_item.json")  + sys.argv[1:], "add_item.json")

except:
    save_to_json_file(sys.argv[1:], "add_item.json")
