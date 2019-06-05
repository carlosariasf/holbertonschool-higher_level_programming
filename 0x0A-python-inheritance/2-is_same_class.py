#!/usr/bin/python3
""" """
def is_same_class(obj, a_class):
    """ """
    if isinstance(obj, a_class):
        if issubclass(a_class, int):
            return isinstance(obj, a_class)
