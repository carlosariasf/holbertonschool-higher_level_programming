#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    count = 0
    dic = a_dictionary.copy()
    for i, j in dic.items():
        if j == value:
            a_dictionary.pop(i, None)
            count += 1
    if count > 0:
        return a_dictionary
    return dic
