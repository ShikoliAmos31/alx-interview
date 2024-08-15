#!/usr/bin/python3
"""
Rotate 2D Matrix by 90 degrees clockwise in-place
"""

def rotate_2d_matrix(matrix):
    """
    Rotate a given n x n 2D matrix 90 degrees clockwise in place.
    
    Args:
        matrix (list of list of int): A 2D list representing the matrix.
        
    Returns:
        None: The matrix is modified in place.
    """
    n = len(matrix)
    
    # Step 1: Transpose the matrix (swap rows and columns)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Step 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()
