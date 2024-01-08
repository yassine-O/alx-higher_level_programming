#!/usr/bin/python3

"""Module 4-inherits_from.py"""


def inherits_from(obj, a_class):
    """ 4-inherits_from documentation """
    return type(obj) is not a_class and issubclass(type(obj), a_class)
