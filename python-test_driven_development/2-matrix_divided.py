#!/usr/bin/python3
'''
    Function that divides
'''


def matrix_divided(matrix, div):
    ''' Function divide,  for j in i] for i in matrix]'''
    new_matrix = []
    error_matrix = "matrix must be a matrix (list of lists) of integers/floats"
    for i in matrix:
        i_len = len(matrix[0])
        for j in i:
            
            if len(i) != i_len:
                raise TypeError("Each i of the matrix must have the same size")
            if type(j) not in [int, float]:
                raise TypeError(error_matrix)
            if type(div) not in [int, float]:
                raise TypeError("div must be a number")
            if div == 0:
                raise ZeroDivisionError("division by zero")
    result = [[round(j / div, 2) for j in i] for i in matrix]
    return result
