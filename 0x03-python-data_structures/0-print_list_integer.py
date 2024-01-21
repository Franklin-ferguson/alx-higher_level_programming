#!/usr/bin/python3


def print_list_integer(my_list=[]):
    my_list = [1, 2, 3, 4, 5]
    count = len(my_list)
    i = 0
    while i <= count:
        print("{}".format(my_list[i]))
        i += 1
print_list_integer()
