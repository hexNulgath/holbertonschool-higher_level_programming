#!/usr/bin/python3
def remove_char_at(str, n):
    i = n
    for letter in str:
        if i == 0:
            continue
        print(f"{letter}", end="")
        i = i - 1
    print()