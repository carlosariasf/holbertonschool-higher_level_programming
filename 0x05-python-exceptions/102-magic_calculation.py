#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    for i in range(a, b):
        try:
            i > a
        except 'Too far':
            result = a ** b / i
