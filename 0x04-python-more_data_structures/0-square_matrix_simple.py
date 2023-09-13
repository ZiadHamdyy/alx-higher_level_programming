#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix2 = []
    for i in range(0, len(matrix)):
        li = []
        for j in range(0, len(matrix[i])):
            li.append(matrix[i][j] * matrix[i][j])
        matrix2.append(li)

    return matrix2
