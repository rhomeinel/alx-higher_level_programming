# 0x04. Python - More Data Structures: Set, Dictionary

## Description
Python - Data Structures

## Table of contents

Files | Description
----------- | -----------
[.gitignore](./.gitignore) | Ignore test files
[0-square_matrix_simple.py](./0-square_matrix_simple.py) | Function that computes the square value of all integers of a matrix. Prototype: def square_matrix_simple(matrix=[]):
[1-search_replace.py](./1-search_replace.py) | Function that replaces all occurrences of an element by another in a new list. Prototype: def search_replace(my_list, search, replace):
[2-uniq_add.py](./2-uniq_add.py) | Function that adds all unique integers in a list (only once for each integer). Prototype: def uniq_add(my_list=[]):
[3-common_elements.py](./3-common_elements.py) | Function that returns a set of common elements in two sets. Prototype: def common_elements(set_1, set_2):
[4-only_diff_elements.py](./4-only_diff_elements.py) | Function that returns a set of all elements present in only one set. Prototype: def only_diff_elements(set_1, set_2):
[5-number_keys.py](./5-number_keys.py) | Function that returns the number of keys in a dictionary. Prototype: def number_keys(a_dictionary):
[6-print_sorted_dictionary.py](./6-print_sorted_dictionary.py) | Function that prints a dictionary by ordered keys. Prototype: def print_sorted_dictionary(a_dictionary):
[7-update_dictionary.py](./7-update_dictionary.py) | Function that replaces or adds key/value in a dictionary. Prototype: def update_dictionary(a_dictionary, key, value):
[8-simple_delete.py](./8-simple_delete.py) | Function that deletes a key in a dictionary. Prototype: def simple_delete(a_dictionary, key=""):
[9-multiply_by_2.py](./9-multiply_by_2.py) | Function that returns a new dictionary with all values multiplied by 2 Prototype: def multiply_by_2(a_dictionary):
[10-best_score.py](./10-best_score.py) | Function that returns a key with the biggest integer value. Prototype: def best_score(a_dictionary):
[11-multiply_list_map.py](./11-multiply_list_map.py) | Function that returns a list with all values multiplied by a number without using any loops. Prototype: def multiply_list_map(my_list=[], number=0):
[12-roman_to_int.py](./12-roman_to_int.py) | Function def roman_to_int(roman_string): that converts a Roman numeral to an integer. Prototype: def roman_to_int(roman_string) must return an integer
[100-weight_average.py](./100-weight_average.py) | Function that returns the weighted average of all integers tuple (<score>, <weight>) Prototype: def weight_average(my_list=[]):
[101-square_matrix_map.py](./101-square_matrix_map.py) | function that computes the square value of all integers of a matrix using map Prototype: def square_matrix_map(matrix=[]):
[102-complex_delete.py](./102-complex_delete.py) | Function that deletes keys with a specific value in a dictionary. Prototype: def complex_delete(a_dictionary, value):
[103-python.c](./103-python.c) | Two (2) C functions that print some basic info about Python lists and Python bytes objects. Prototype 1: void print_python_list(PyObject *p); Prototype 2: void print_python_bytes(PyObject *p); shared library will be compiled with this command line: ``` gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 103-python.c ```
[103-tests.py](./103-tests.py) | Task 16 file
