#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    length = len(argv)

    
    if length == 1:
        print("{} arguments.".format(0))
    elif length == 2:
        print("{} argument:".format(length))
        print("1: {}".format(argv[1]))
    elif length > 2:
        print("{} arguments:".format((length)))
        for i in range(1, length):
            print("{}: {}".format(i, argv[i]))
