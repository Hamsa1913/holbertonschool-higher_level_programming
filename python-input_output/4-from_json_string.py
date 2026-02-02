#!/usr/bin/python3
"""Converts a JSON string to a Python object."""

import json

# Converts a JSON string to a Python object
# Returns a list or dict depending on the input
def from_json_string(my_str):
    return json.loads(my_str)
