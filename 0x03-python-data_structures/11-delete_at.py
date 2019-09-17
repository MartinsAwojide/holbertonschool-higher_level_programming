#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    for x in my_list:
        if idx == my_list.index(x):
            my_list.remove(x)
            return (my_list)
        elif idx >= len(my_list):
            return (my_list)
        elif idx < 0:
            return (my_list)
