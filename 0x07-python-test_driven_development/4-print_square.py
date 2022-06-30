#!/usr/bin/python3
"""
Module print_square
Defines a function that prints a square with the character #.
"""


def print_square(size):
    """
    size is the length of the square, size must be integer
    otherwise raise a ValueError exception
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print('#', end='')
        print()
