#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        for i in range(x):
            print("{:d}".format(my_list[i]), end="")
        print("")
        return my_list[i]
    except:
        print("")
        return i
