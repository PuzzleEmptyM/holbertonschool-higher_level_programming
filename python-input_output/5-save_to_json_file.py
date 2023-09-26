#!/usr/bin/python3
""" save_to_json_file module """
import json


def save_to_json_file(my_obj, filename):
    """ writes JSON object dump to file """
    with open(filename, 'w', encoding="utf8") as f:
        f.write(json.dumps(my_obj))
