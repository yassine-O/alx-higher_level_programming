#!/usr/bin/python3

""" Module 1-write_file.py """

import json


def save_to_json_file(my_obj, filename):
    """ 1-write_file documentation """
    with open(filename, 'w', encoding="utf-8") as file:
        json.dump(my_obj, file)
