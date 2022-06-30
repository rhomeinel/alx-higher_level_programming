#!/usr/bin/python3
"""
Module say_my_name
Define a function that prints first name and last name
"""


def say_my_name(first_name, last_name=""):
    """
    print first name and last name.
    Raise TypeError if the name is not a string
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
