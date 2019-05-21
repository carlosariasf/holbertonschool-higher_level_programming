#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    try:
        return fct(args[0], args[1])
    except Exception as e:
        print("Exception:", e, file=stderr)
        return None
