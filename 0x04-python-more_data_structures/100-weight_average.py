#!/usr/bin/python3
def weight_average(my_list=[]):
    result1 = 0
    result2 = 0
    if my_list:
        for i in my_list:
            result1 += i[0] * i[1]
            result2 += i[1]
        return result1 / result2
    else:
        return 0
