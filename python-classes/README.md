Python – Classes

This project introduces Object-Oriented Programming (OOP) in Python by progressively building a Square class with increasing levels of complexity.
Through this project, you will learn how to design classes, manage attributes, validate data, and apply core OOP principles in a Pythonic way.

Learning Objectives

By the end of this project, you should be able to explain, without external help:

What Object-Oriented Programming (OOP) is

What a class, object, and instance are

The difference between a class and an object or instance

What an attribute is and the difference between public, protected, and private attributes

How to use self

What a method is and the purpose of the special __init__ method

The concepts of Data Abstraction, Data Encapsulation, and Information Hiding

How to use properties, getters, and setters in Python

| Task | Description                                               |
| ---: | --------------------------------------------------------- |
|    0 | Create an empty `Square` class                            |
|    1 | Add a private `size` attribute                            |
|    2 | Validate `size` as an integer greater than or equal to 0  |
|    3 | Add an `area()` method to calculate the square’s area     |
|    4 | Add getter and setter methods for `size` with validation  |
|    5 | Add a `my_print()` method to print the square using `#`   |
|    6 | Add a `position` attribute to control the printing offset |
How to validate attributes and control access to them
Requirements

Python 3.8 or higher

All files must be executable and start with:
#!/usr/bin/python3
Code must follow pycodestyle

Each module, class, and method must include a meaningful docstring

No external modules may be imported
Example Usage
from square import Square

s = Square(3, (1, 2))
print(s.size)      # 3
print(s.position)  # (1, 2)
print(s.area())    # 9
s.my_print()
Author : HAMSA ALAMMAR
