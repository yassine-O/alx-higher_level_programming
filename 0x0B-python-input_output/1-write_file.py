#!/usr/bin/python3

""" Module 1-write_file.py """


def write_file(filename="", text=""):
    """ 1-write_file documentation """
    with open(filename, 'w', encoding="utf-8") as file:
        return file.write(text)
