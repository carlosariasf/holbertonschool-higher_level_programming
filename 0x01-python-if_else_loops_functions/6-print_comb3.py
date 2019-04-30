#!/usr/bin/python3
for c in range(1, 100):
    if (c % 10) > (c / 10) and c != 89:
        print("{:02d}, ".format(c), end="")
    elif (c % 10) > (c / 10) and c == 89:
        print("{:02d}".format(c))
