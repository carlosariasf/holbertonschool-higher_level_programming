#!/usr/bin/python3
"""function that finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """find a peak"""
    tmp = 0
    for i in range(len(list_of_integers)):
        if list_of_integers[i] > tmp:
            tmp = list_of_integers[i]
    result = None if tmp == 0 else tmp
    return result
