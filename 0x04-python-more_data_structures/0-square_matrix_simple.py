#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    thematrix = matrix.copy()
    for i in range(len(matrix)):
        thematrix[i] = list(map(lambda x: x**2, matrix[i]))
    return thematrix
