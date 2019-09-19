#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = {}
    for keys, values in a_dictionary.items():
        new[keys] = values * 2
    return new
