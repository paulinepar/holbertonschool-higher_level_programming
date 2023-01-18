#!/usr/bin/python3
def print_last_digit(number):

    last = number % 10
    last_neg = number % (-10) * (-1)

    if number < 0:
        print("{:d}".format(last_neg), end="")
        return(last_neg)
    if number >= 0:
        print("{:d}".format(last), end="")
        return(last)
