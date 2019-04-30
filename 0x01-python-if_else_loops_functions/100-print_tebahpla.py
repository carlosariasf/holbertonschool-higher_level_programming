#!/usr/bin/python3
control = 0
char = ""
for c in range(122, 96, -1):
    if control == 1:
        char = chr(c - 32)
        control = 0
    else:
        char = chr(c)
        control = 1
    print("{}".format(char), end="")
