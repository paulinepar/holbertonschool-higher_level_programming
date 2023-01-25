#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mama_matrix = []
    for each_list in matrix:
        new_list = []
        for element in each_list:
            new_list.append(element*element)
        mama_matrix.append(new_list)
    return mama_matrix
