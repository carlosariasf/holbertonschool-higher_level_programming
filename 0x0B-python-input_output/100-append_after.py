#!/usr/bin/python3
""" """


def append_after(filename="", search_string="", new_string=""):
    """ """
    newstr = ''
    oldidx = 0
    with open(filename, mode='r', encoding='utf-8') as f:
        text = f.read()
        idx = text.find(search_string)
        if idx >= 0:
            for i in range(idx, len(text)):
                if text[i-1] == '\n':
                    newstr = text[0:i] + new_string
                    oldidx = i
        newstr = newstr + text[oldidx:]
    with open(filename, mode='w', encoding='utf-8') as f:
        f.write(newstr)
