#!/usr/bin/python3

"""Declaring a class Square"""


class Square:

    def __init__(self, size=0):
        if not instance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
