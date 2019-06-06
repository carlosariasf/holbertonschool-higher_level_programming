#!/usr/bin/python3
""" """


def number_of_lines(filename=""):
    """ """
    lines = 0
    with open(filename, encoding='utf-8') as filet:
        while True:
            line = filet.readline()
            if not line:
                break
            lines += 1
    return lines
