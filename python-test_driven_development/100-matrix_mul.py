#!/usr/bin/python3
"""Matrix multiplication module"""


def matrix_mul(m_a, m_b):
    """Multiplies two matrices and returns the result"""
    # Check types
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if len(m_a) == 0 or any(len(row) == 0 for row in m_a):
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or any(len(row) == 0 for row in m_b):
        raise ValueError("m_b can't be empty")
    # Check all elements are numbers
    for row in m_a:
        if not all(isinstance(i, (int, float)) for i in row):
            raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        if not all(isinstance(i, (int, float)) for i in row):
            raise TypeError("m_b should contain only integers or floats")
    # Check rows have same size
    row_len_a = len(m_a[0])
    if not all(len(row) == row_len_a for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    row_len_b = len(m_b[0])
    if not all(len(row) == row_len_b for row in m_b):
        raise TypeError("each row of m_b must be of the same size")
    # Check multiplication possibility
    if row_len_a != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    # Perform multiplication
    result = []
    for row in m_a:
        new_row = []
        for j in range(len(m_b[0])):
            s = 0
            for k in range(len(m_b)):
                s += row[k] * m_b[k][j]
            new_row.append(s)
        result.append(new_row)
    return result
