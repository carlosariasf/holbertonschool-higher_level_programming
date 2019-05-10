#!/usr/bin/python3
def roman_to_int(roman_string):
    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sumr = 0
    nstr = roman_string
    tmp = 0
    for i in range(len(nstr)):
        tmp = romans[nstr[i]]
        if i+1 < len(nstr) and romans[nstr[i+1]] > tmp:
            sumr -= tmp
        else:
            sumr += tmp
    return sumr
