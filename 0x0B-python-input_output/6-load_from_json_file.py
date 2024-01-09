#!/usr/bin/python3

""" Module 1-write_file.py """

import json


def load_from_json_file(filename):
    """ 1-write_file documentation """
    with open(filename, 'r', encoding="utf-8") as file:
        return json.load(file)
