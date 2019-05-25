#!/usr/bin/python3
"""Python Module

    Functions:
        print_square(size)
"""
def print_square(size):
    """Function to print a square

    Args:
        size: Size of square
    """
    try:
        try:
            if type(size) != int:
                raise TypeError
        except TypeError as e:
            raise Exception("size must be an integer") from e
        try:
            if (int(size) < 0):
                raise ValueError
            else:
                for i in range(size):
                    for j in range(size):
                        print("#", end='')
                    print("")
        except TypeError as e:
            raise Exception("size must be >= 0") from e
    except Exception as err:
        print(err)
