#A function that takes a string and an integer as an argument.

import re


def print_many_times(text, times):
    result = 1
    while result <= times:
        print(text)
        result += 1


print_many_times("Python", 4)
