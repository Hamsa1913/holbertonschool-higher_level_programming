# Python Test-Driven Development

## Project Overview
This repository contains Python functions developed following **Test-Driven Development (TDD)** principles. Each function is tested using `doctest` to ensure correctness and reliability.

## Tasks

### 0. Integers Addition
**File:** `0-add_integer.py`  
**Function:** `add_integer(a, b=98)`  

**Description:**  
Adds two integers and returns the result.  

**Requirements:**  
- `a` and `b` must be integers or floats, otherwise a `TypeError` is raised with the message:
  - `"a must be an integer"` or `"b must be an integer"`
- If floats are provided, they are cast to integers before addition.
- Returns the sum as an integer.
- No modules are imported.

**Usage Example:**
```python
>>> add_integer(1, 2)
3
>>> add_integer(100, -2)
98
>>> add_integer(2)
100
>>> add_integer(100.3, -2)
98
>>> add_integer(4, "School")
Traceback (most recent call last):
    ...
TypeError: b must be an integer
>>> add_integer(None)
Traceback (most recent call last):
    ...
TypeError: a must be an integer
