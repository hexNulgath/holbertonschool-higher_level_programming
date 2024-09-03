#!/usr/bin/env python3
def uppercase(str):
    for letter in str:
        if ord(letter) >= ord('a') and ord(letter) <= ord('z'):
            upper= chr(ord(letter) - 32)
        else:
            upper = letter
        print("{}".format(upper), end="")
    print()
