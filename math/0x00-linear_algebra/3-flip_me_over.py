#!/usr/bin/env python3
"""This module contains the function matrix_transpose"""


def matrix_transpose(matrix):
    """returns the transpose of a 2d matrix"""
    transpose = []
    for i in range(len(matrix[0])):
        transpose.append([])
        for j in range(len(matrix)):
            transpose[i].append(matrix[j][i])
    return transpose
