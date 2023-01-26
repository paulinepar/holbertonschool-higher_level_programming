#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if key == 0:
        return
    else:
        a_dictionary.update({key: value})
    return a_dictionary