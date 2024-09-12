#!/usr/bin/python3
def roman_to_int(roman_string):
    decimal = 0
    roman_decimal = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if not isinstance(roman_string, str):
        return 0
    for i in range(len(roman_string) - 1):
        if roman_decimal[roman_string[i]] >= roman_decimal[roman_string[i + 1]]:
            decimal += roman_decimal[roman_string[i]]
        else:
            decimal -= roman_decimal[roman_string[i]]
    decimal += roman_decimal[roman_string[-1]]
    return decimal
