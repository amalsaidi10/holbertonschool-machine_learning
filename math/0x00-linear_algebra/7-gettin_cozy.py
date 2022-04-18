#!/usr/bin/env python3
"""function to concatenate matrices"""


def cat_matrices2D(mat1, mat2, axis=0):
    """concatenate mat1 and mat2 along a specific axis"""
    if axis > 1:
        return None
    elif axis == 1:# add in row 
        if len(mat1) != len(mat2) or not len(mat1):  
            return None
        mat = []
        for i in range(len(mat1)):
            mat.append([])
            mat[i] = mat1[i] + mat2[i]
    else: #add in coloumn 
        if not len(mat1) or not len(mat2) or len(mat1[0]) != len(mat2[0]):
            return None
        mat = []
        for row in mat1:
            mat.append(row.copy())
        for row in mat2:
            mat.append(row.copy())
    return mat
  
