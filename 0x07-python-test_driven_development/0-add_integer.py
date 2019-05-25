#!/usr/bin/python3
"""Module add_integer

    Functions:
    add_integer(a,b)
"""

def add_integer(a, b=98):
    """
    Function to add int
    """
    try:
        if type(a) is int or type(a) is float:
            a = int(a)
        else:
            raise TypeError
    except TypeError as e:
        raise Exception("a must be an integer") from e
    try:
        if type(b) is int or type(b) is float:
            b = int(b)
        else:
            raise TypeError
    except TypeError as e:
        raise Exception("b must be an integer") from e
    return a + b
