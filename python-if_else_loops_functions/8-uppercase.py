#!/usr/bin/python3
def uppercase(str):
    # iterer la string
    for s in str:
        # verifie si c'est une lower
        if ord(s) >= 97 and ord(s) <=122:
            transfo = ord(s) - 32
        else:
            transfo = ord(s)

        print("{}".format(chr(transfo)), end="")
print()
