#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mama_matrix = []
    # parcoure ma matrix (list)
    for each_list in matrix:
        # parcoure list dans list
        new_list = []
        for element in each_list:
            #ajoute *j achaque element a new_list
            new_list.append(element*element)
        mama_matrix.append(new_list)
    return mama_matrix
