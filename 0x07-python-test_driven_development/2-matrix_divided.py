#!/usr/bin/python3
"""Python Module

    Functions:
        matrix_divided(matrix, div)
"""
def matrix_divided(matrix, div):
    """Function to div a matrix

    Args:
        matrix: Matrix of numbers
        div: Number to div the matrix
        Return: New matrix
    """
    count = 0
    itms = 0
    tmp = []
    newm = []
    try:
        try:
            if type(div) is int or type(div) is float:
                pass
            else:
                raise TypeError
        except TypeError as e:
            raise Exception("div must be a number")
        try:
            if div == 0:
                raise ZeroDivisionError
        except ZeroDivisionError as e:
            raise Exception("division by zero") from e
        try:
            if len(matrix) < 2:
                raise TypeError
            for i in range(len(matrix)):
                for j in range(len(matrix[i])):
                    if type(matrix[i][j]) is int or type(matrix[i][j]) is float:
                        tmp.append(round(matrix[i][j] / div, 2))
                        count += 1
                    else:
                        raise TypeError
                newm.append(tmp)
                tmp = []
        except TypeError as e:
            raise Exception("matrix must be a matrix (list of lists) of"
                            " integers/floats") from e
        try:
            if count % len(matrix) != 0:
                raise TypeError
        except TypeError as e:
            raise Exception("Each row of the matrix must have the same "
                            "size") from e
    except Exception as err:
        print(err)

    return newm
