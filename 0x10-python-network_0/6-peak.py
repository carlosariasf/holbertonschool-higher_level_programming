#!/usr/bin/python3
"""function that finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """find a peak"""
    if len(list_of_integers) < 1:
        return None
    else:
        return max(list_of_integers)
