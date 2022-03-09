
#!/usr/bin/env python3
def determinant(matrix):
  
    if type(matrix) is not list or not matrix:
        raise TypeError('matrix must be a list of lists')
    # convention   
    if matrix == [[]]:
        det=1
    # else ,we calculate the determinant with formula    
    else:
      #else found the determinant    
      m = len(matrix)
      for row in matrix:
          if type(row) is not list:
              raise TypeError('matrix must be a list of lists')
          if len(row) != m:
              raise ValueError('matrix must be a square matrix')
      if m == 1:
          return matrix[0][0]
      #construct sub_matrix
      sub_matrix = []
      for i in range(m - 1):
          row = []
          for j in range(m - 1):
              row.append(0)
          sub_matrix.append(row)  # here we obtain a submatrix with shape m-1 * m-1 and all values are equal to zero 

      det = 0
      for i in range(m): # here traverse the columns
          val = matrix[0][i] #(a_0,j)
          for j in range(m - 1):
              for k in range(m - 1):
                  if k < i:
                      sub_matrix[j][k] = matrix[j + 1][k]
                  else:
                      sub_matrix[j][k] = matrix[j + 1][k + 1]
          sub_det = determinant(sub_matrix)
          det += ((-1) ** i) * val * sub_det   # using the formula
    return det
