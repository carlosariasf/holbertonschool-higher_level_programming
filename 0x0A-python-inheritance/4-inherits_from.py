#!/usr/bin/python3
""" """


def inherits_from(obj, a_class):
    """ """
    if not issubclass(a_class, type(obj)):
        return isinstance(obj, a_class)
