#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary:
        dic = a_dictionary.copy()
        for i, j in dic.items():
            if j == value:
                dic = a_dictionary.pop(i, None)
        return a_dictionary
    return None
