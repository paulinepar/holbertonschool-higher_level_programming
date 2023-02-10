#!/usr/bin/python3
'''
    Create a function def pascal_triangle(n): that returns a
    list of lists of integers representing the Pascal’s triangle of n:
'''


def pascal_triangle(n):
    '''function that return triangle pascal'''
    list = [1]
    if n <= 0:
        return list
    for i in range(n):
        print(list)
        newlist = []
        newlist.append(list[0])
        for i in range(len(list) - 1):
            newlist.append(list[i] + list[i + 1])
        newlist.append(list[- 1])
        list = newlist
    return newlist
