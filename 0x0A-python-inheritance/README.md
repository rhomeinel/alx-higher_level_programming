# 0x0A. Python - Inheritance

## Description
This directory  is an introduction to the concept of ``` inheritance ``` .

- Inheritance is a mechanism in which one class acquires the property of another class. For example, a child inherits the traits of his/her parents. With inheritance, we can reuse the fields and methods of the existing class. Hence, inheritance facilitates Reusability and is an important concept of OOPs.


## Table of contents

Files | Description
----------- | -----------
[.gitignore](./.gitignore) | Ignore test files
[0-lookup.py](./0-lookup.py) | Function that returns the list of available attributes and methods of an object: Prototype: def lookup(obj):
[1-my_list.py](./1-my_list.py) | A class MyList that inherits from list: Public instance method: def print_sorted(self): that prints the list, but sorted (ascending sort)
[2-is_same_class.py](./2-is_same_class.py) | Function that returns True if the object is exactly an instance of the specified class ; otherwise False. Prototype: def is_same_class(obj, a_class):
[3-is_kind_of_class.py](./3-is_kind_of_class.py) | Function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False. Prototype: def is_kind_of_class(obj, a_class):
[4-inherits_from.py](./4-inherits_from.py) | Function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False. Prototype: def inherits_from(obj, a_class):
[5-base_geometry.py](./5-base_geometry.py) | An empty class BaseGeometry
[6-base_geometry.py](./6-base_geometry.py) | A class BaseGeometry (based on 5-base_geometry.py). Public instance method: def area(self): that raises an Exception with the message area() is not implemented
[7-base_geometry.py](./7-base_geometry.py) | A class BaseGeometry (based on 6-base_geometry.py). Public instance method: def area(self): that raises an Exception with the message area() is not implemented / Public instance method: def integer_validator(self, name, value): that validates value
[8-rectangle.py](./8-rectangle.py) | A class Rectangle that inherits from BaseGeometry (7-base_geometry.py). Instantiation with width and height: def __init__(self, width, height):
[9-rectangle.py](./9-rectangle.py) | A class Rectangle that inherits from BaseGeometry (7-base_geometry.py). (task based on 8-rectangle.py). Instantiation with width and height: def __init__(self, width, height):
[10-square.py](./10-square.py) | A class Square that inherits from Rectangle (9-rectangle.py). Instantiation with size: def __init__(self, size):
[11-square.py](./11-square.py) | A class Square that inherits from Rectangle (9-rectangle.py). (task based on 10-square.py). Instantiation with size: def __init__(self, size):
[100-my_int.py](./100-my_int.py) | A class MyInt that inherits from int:
[101-add_attribute.py](./101-add_attribute.py) | A function that adds a new attribute to an object if it’s possible: 


## Resources
- [Inheritance](https://docs.python.org/3/tutorial/classes.html#inheritance)
- [Inheritance in Python](https://www.packt.com/inheritance-python/)
- [Learn to Program 10 : Inheritance Magic Methods](https://www.youtube.com/watch?v=d8kCdLCi6Lk)
