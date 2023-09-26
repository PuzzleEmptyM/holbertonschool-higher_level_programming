#!/usr/bin/python3
""" script add_item adds arguments as list, then saves to file """
import json
from sys import argv
jsonsave = __import__('5-save_to_json_file').save_to_json_file
jsonload = __import__('6-load_from_json_file').load_from_json_file


try:
    risuto = jsonload('add_item.json')
except:
    risuto = []
finally:
    jsonsave(risuto + argv[1:], 'add_item.json')
