#!/usr/bin/python3

"""Module 0-square"""


class Square:
    """Square documentation"""

    def __init__(self, size=0):
        """Initializes the data."""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
