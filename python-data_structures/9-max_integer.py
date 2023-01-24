#!/usr/bin/python3
def max_integer(my_list=[]):
    lenght = len(my_list)
    max = my_list[0]
    if lenght == 0:
        return None
    if my_list == 0:
        return None
    for i in my_list:
        if i > max:
            max = i
    return max
