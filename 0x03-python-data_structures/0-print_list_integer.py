#!/usr/bin/python3


def print_list_integer(my_list=[]):
    count = len(my_list) - 1
    i = 0
    while i <= count:
        print("{:d}".format(my_list[i]))
        i += 1
print_list_integer()
