#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    count = 0
    for i, j in sorted(a_dictionary.items()):
        if i == key:
            a_dictionary[i] = value
    if count == 0:
            a_dictionary[key] = value
    return a_dictionary
