#!/usr/bin/python3

""" Module 1-write_file.py """

import json


def class_to_json(obj):
    """ 1-write_file documentation """
    print("=>", obj.__dict__)
    return json.dumps(obj.__dict__)
