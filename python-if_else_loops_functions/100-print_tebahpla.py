#!/usr/bin/python3
for letter in (122, 96, -1):
    if letter % 2 == 0:
        letter = letter - 32    
    print("{}".format(chr(letter)), end="")
