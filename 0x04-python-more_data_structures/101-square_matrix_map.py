#!/usr/bin/python3
    matrix2 = map(list, matrix)
    return list(map(lambda x: (x[0]*x[0], x[1]*x[1], x[2]*x[2]), matrix2))
