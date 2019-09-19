#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for keys in sorted(a_dictionary.items()):
        print("{}: {}".format(keys[0], keys[1]))
