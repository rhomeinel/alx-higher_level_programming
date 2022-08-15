# 0x03. Python - Data Structures: Lists, Tuples

## Description
Data Structures: Lists, Tuples

## Table of contents

Files | Description
----------- | -----------
[.gitignore](./.gitignore) | Ignore test files.
[0-print_list_integer.py](./0-print_list_integer.py) | Function that prints all integers of a list. Prototype: def print_list_integer(my_list=[]):
[1-element_at.py](./1-element_at.py) | function that retrieves an element from a list like in C. Prototype: def element_at(my_list, idx):
[2-replace_in_list.py](./2-replace_in_list.py) | Function that replaces an element of a list at a specific position (like in C). Prototype: def replace_in_list(my_list, idx, element):
[3-print_reversed_list_integer.py](./3-print_reversed_list_integer.py) | Function that prints all integers of a list, in reverse order. Prototype: def print_reversed_list_integer(my_list=[]):
[4-new_in_list.py](./4-new_in_list.py) | Function that replaces an element in a list at a specific position without modifying the original list (like in C). Prototype: def new_in_list(my_list, idx, element):
[5-no_c.py](./5-no_c.py) | Function that removes all characters c and C from a string. Prototype: def no_c(my_string):
[6-print_matrix_integer.py](./6-print_matrix_integer.py) | Function that prints a matrix of integers. Prototype: def print_matrix_integer(matrix=[[]]):
[7-add_tuple.py](./7-add_tuple.py) | Function that adds 2 tuples. Prototype: def add_tuple(tuple_a=(), tuple_b=()):
[8-multiple_returns.py](./8-multiple_returns.py) | Function that returns a tuple with the length of a string and its first character. Prototype: def multiple_returns(sentence):
[9-max_integer.py](./9-max_integer.py) | Function that finds the biggest integer of a list. Prototype: def max_integer(my_list=[]):
[10-divisible_by_2.py](./10-divisible_by_2.py) | Function that finds all multiples of 2 in a list. Prototype: def divisible_by_2(my_list=[]):
[11-delete_at.py](./11-delete_at.py) | Function that deletes the item at a specific position in a list. Prototype: def delete_at(my_list=[], idx=0):
[12-switch.py](./12-switch.py) | Completes the source code in order to switch value of a and b (https://github.com/holbertonschool/0x03.py/blob/master/12-switch_py)
[lists.h](./lists.h) | Header for task 13
[linked_lists.c](./linked_lists.c) | C file for task 13
[palindrome](./palindrome) | Compiled code for task 13
[13-is_palindrome.c](./13-is_palindrome.c) | Function in C that checks if a singly linked list is a palindrome. Prototype: int is_palindrome(listint_t **head);
[100-print_python_list_info.c](./100-print_python_list_info.c) | C function that prints some basic info about Python lists. Prototype: void print_python_list_info(PyObject *p); Shared library will be compiled with this command line:```   gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,PyList -o libPyList.so -fPIC -I/usr/include/python3.4 100-print_python_list_info.c ```
