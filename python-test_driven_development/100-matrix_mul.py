#!/usr/bin/python3
"""
Matrix multiplication module
"""


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices
    """
    # Check if m_a and m_b are lists
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # Check if m_a and m_b are lists of lists
    if any(not isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if any(not isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    # Check if m_a and m_b are not empty
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    # Check all elements are int or float
    for row in m_a:
        if any(not isinstance(x, (int, float)) for x in row):
            raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        if any(not isinstance(x, (int, float)) for x in row):
            raise TypeError("m_b should contain only integers or floats")

    # Check all rows are same size
    if any(len(row) != len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if any(len(row) != len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    # Check if matrices can be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform multiplication
    result = []
    for i in range(len(m_a)):
        new_row = []
        for j in range(len(m_b[0])):
            s = 0
            for k in range(len(m_b)):
                s += m_a[i][k] * m_b[k][j]
            new_row.append(s)
        result.append(new_row)
    return result
