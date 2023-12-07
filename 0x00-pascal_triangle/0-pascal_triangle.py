#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """
    This module defines the function pascal_triangle(n),
    which generates Pascal's triangle up to the specified number of rows.

    Args:
        n (int): The number of rows to generate for Pascal's triangle.

    Returns:
        list: A list of lists representing Pascal's triangle.
        Each inner list corresponds to a row in the triangle.

    Note:
        - If n is less than or equal to 0, an empty list is returned.
        - The triangle is constructed based on the principle that
          each number is the sum of the two numbers directly above it in the row above.
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        if i > 1:
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle
