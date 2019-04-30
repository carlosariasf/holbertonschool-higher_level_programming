#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        if i + 1 < len(str):
            endo = ""
        else:
            endo = "\n"
        if ord(str[i]) > 96 and ord(str[i]) < 123:
            print("{}".format(chr(ord(str[i]) - 32)), end=endo)
        else:
            print("{}".format(str[i]), end=endo)
