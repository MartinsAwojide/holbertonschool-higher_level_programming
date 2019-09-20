#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    num = 0
    den = 0
    for number in my_list:
        num += number[0] * number[1]
        den += number[1]
    return num/den
