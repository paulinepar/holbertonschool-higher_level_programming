#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    key = dict(sorted(a_dictionary.items()))
    print("{}".format(key))
