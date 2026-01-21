"""Module that prints a square with '#' characters"""

def print_square(size):
    """Prints a square of size 'size' using '#' characters"""
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
