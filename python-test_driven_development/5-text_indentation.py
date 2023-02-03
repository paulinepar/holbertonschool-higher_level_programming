#!/usr/bin/python3
'''
    create function text_indentation
'''


def text_indentation(text):
    '''function that print a text with 2 lines after each of these characters: .,?,:'''
    
    special = False
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in text:
        if i in [".", ":", "?"]:
            print(i)
            print()
            special = True
        else:
            if special and i == ' ':
                pass
            else:
                special = False
                print(i, end='')
