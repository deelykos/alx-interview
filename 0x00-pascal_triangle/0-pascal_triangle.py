#!/usr/bin/python3
"""
0-pascal_triangle

This module defines the function pascal_triangle(n), which generates Pascal's triangle up to the specified number of rows.

Args:
    n (int): The number of rows to generate for Pascal's triangle.

Returns:
    list: A list of lists representing Pascal's triangle. Each inner list corresponds to a row in the triangle.

Note:
    - If n is less than or equal to 0, an empty list is returned.
    - The triangle is constructed based on the principle that each number is the sum of the two numbers directly above it in the row above.
"""

def pascal_triangle(n):
    if n <= 0:
        return []
    
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])

        row.append(1)
        triangle.append(row)

    return triangle