#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    if my_list is None:
        return 0
    count = 0
    try:
        for i in range(x):
            print("{:d}".format(my_list[i], end=""))
            count = count + 1
    except (ValueError, TypeError):
        pass
    return count
