#!/usr/bin/pyth0n3
"""
Module 2-square
Defines class Square with private attribute size and validates size
"""


class Square:
    """
    class Square definition
    Args:
        size (int): size of a side in square
    """
    def __init__(self, size=0):
        """
        Initializes square
        Attributes:
            __size (int): size of new square, default is 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
