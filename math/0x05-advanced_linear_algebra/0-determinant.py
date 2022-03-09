
#!/usr/bin/env python3

def determinant(matrix):
    if type(matrix) is not list or not matrix:
        raise TypeError('matrix must be a list of lists')
    if matrix == [[]]:
        return 1
    m = len(matrix)
    for row in matrix:
        if type(row) is not list:
            raise TypeError('matrix must be a list of lists')
        if len(row) != m:
            raise ValueError('matrix must be a square matrix')
    if m == 1:
        return matrix[0][0]

    sub_matrix = []
    for i in range(m - 1):
        row = []
        for j in range(m - 1):
            row.append(0)
        sub_matrix.append(row)

    det = 0
    for i in range(m):
        val = matrix[0][i]
        for j in range(m - 1):
            for k in range(m - 1):
                if k < i:
                    sub_matrix[j][k] = matrix[j + 1][k]
                else:
                    sub_matrix[j][k] = matrix[j + 1][k + 1]
        sub_det = determinant(sub_matrix)
        det += ((-1) ** i) * val * sub_det
    return det
