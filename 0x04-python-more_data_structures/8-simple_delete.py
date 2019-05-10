#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    count = 0
    for i, j in sorted(a_dictionary.items()):
        if i == key:
            a_dictionary.pop(key, None)
    return a_dictionary
