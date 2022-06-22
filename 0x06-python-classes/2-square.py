#!/usr/bin/pyth0n3
"""
Module 2-square
Defines class Square with private size and validates size
"""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """
        Initializes square
        Attributes:
            size (int): size=0
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
