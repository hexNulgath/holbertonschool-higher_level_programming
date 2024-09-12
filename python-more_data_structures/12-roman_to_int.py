#!/usr/bin/python3
def roman_to_int(roman_string):
    decimal = 0
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if not isinstance(roman_string, str):
        return 0
    for i in range(len(roman_string) - 1):
        if d[roman_string[i]] >= d[roman_string[i + 1]]:
            decimal += d[roman_string[i]]
        else:
            decimal -= d[roman_string[i]]
    decimal += d[roman_string[-1]]
    return decimal
