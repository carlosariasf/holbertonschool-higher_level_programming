#!/usr/bin/python3
def uppercase(str):
    str2 = ""
    for i in range(0, len(str)):
            if ord(str[i]) > 96 and ord(str[i]) < 123:
                str2 += chr(ord(str[i]) - 32)
            else:
                str2 += str[i]
    print("{}".format(str2))
