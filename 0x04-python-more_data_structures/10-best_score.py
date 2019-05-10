#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        dic2 = a_dictionary.copy()
        dic2 = sorted((value, key) for (key, value) in dic2.items())
        dic2 = sorted(dic2)
        return dic2[len(dic2)-1][1]
    return None
