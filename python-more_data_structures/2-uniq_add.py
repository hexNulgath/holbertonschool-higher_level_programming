#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    result = 0
    for i in range(len(my_list)):
        if my_list[i] not in new_list:
            new_list.append(my_list[i])
    for j in range(len(new_list)):
        result += new_list[j]
    return result
