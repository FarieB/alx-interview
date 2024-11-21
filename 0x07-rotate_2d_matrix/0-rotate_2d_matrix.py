#!/usr/bin/python3
"""
Rotate a 2D matrix by 90 degrees clockwise.
"""

def rotate_2d_matrix(matrix):
    """
    Rotates an n x n 2D matrix 90 degrees clockwise.
    The matrix is modified in-place, and nothing is returned.

    Args:
        matrix (list of list of ints): The 2D matrix to rotate.
    """
    n = len(matrix)
    
    # Transpose the matrix (swap rows and columns)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Reverse each row
    for row in matrix:
        row.reverse()
