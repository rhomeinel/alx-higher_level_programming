#!/usr/bin/python3
"""
Module 2-append_write
Append a string at the end of a text file and returns the number of charaters.
"""


def append_write(filename="", text=""):
    """
    Append text to filename.

    Args:
        - filename: name of the file
        - text: text to append
    Returns: the number of characters added
    """

    with open(filename, "a" encoding="utf-8")as f:
        return f.write(text)
