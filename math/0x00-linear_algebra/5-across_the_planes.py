#!/usr/bin/env python3
"""
adds two matrices element-wise
"""


def add_matrices2D(mat1, mat2):
"""adds matrives"""
  new_matrix = []
  if len(mat1[0])!= len(mat2[0]):
    return None
  
  for i in range(len(mat1)):
    new_matrix.append([])
    for j in range(len(mat1[i])):

      new_matrix[i].append(mat1[i][j] + mat2[i][j])
  return new_matrix
  
