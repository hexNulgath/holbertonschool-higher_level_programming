#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    d = sorted(a_dictionary)
    for key in d:
        print(f"{key}: {a_dictionary[key]}")
