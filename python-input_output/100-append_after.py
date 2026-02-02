#!/usr/bin/python3
"""Insert a line after lines containing a specific string in a file."""


def append_after(filename="", search_string="", new_string=""):
    """Insert new_string after every line containing search_string."""
    with open(filename, "r") as f:
        lines = f.readlines()

    with open(filename, "w") as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
