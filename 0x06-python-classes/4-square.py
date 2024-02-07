#!/usr/bin/python3

"""Declaring a class called Square."""


class Square:
    """represent a class Square."""

    def __init__(self, size=0):
        """intialize a new square.
        Args:
            size (int): The size of the new square.
        """

        self.size = size

    @property
    def size(self):
        """this gets the size of the square"""
        return(self.__size)


    @size.setter
    def size(self, val):
            
        if not isinstance(val, int):
            raise TypeError("size must be an integer")
        elif val < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the area of the square"""
        return (self.__size * self.__size)
