#!/usr/bin/python3
def remove_char_at(str, n):
    result = ""
    length = len(str)
    for i in range(length):
        if i == n:
            continue
        result += str[i]
    return result
