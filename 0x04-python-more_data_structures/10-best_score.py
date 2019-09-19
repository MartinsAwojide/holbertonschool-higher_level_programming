#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    elif len(a_dictionary) is 0:
        return None
    else:
        return (max(a_dictionary))
