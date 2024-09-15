#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    result = 0
    weight = 0
    for tuple in my_list:
        result += tuple[0] * tuple[1]
        weight += tuple[1]
    result = result / weight
    return result
