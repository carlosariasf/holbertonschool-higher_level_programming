#!/usr/bin/python3
def magic_calculation(a, b, c):
    if (a < b):
        return False
    elif (c > b):
        return False
    else:
        return (a * b) - c
