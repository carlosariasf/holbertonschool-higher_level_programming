#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dic2 = a_dictionary.copy()
    for i, j in sorted(dic2.items()):
            dic2[i] = j*2
    return dic2
