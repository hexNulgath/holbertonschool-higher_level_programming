#!/usr/bin/python3
""""
    Splits the given text at every '.', '?', or
    ':', printing each part with two newlines.
"""


def text_indentation(text):
    """
    Parameters:
        text (str): The text to process.

    Raises:
        TypeError: If text is not a string.

    Example:
        >>> text_indentation("Hello. How are you? I'm fine.")
        Hello.

        How are you?

        I'm fine.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_line = False
    for letter in text:
        if letter in '.?:':
            print(f"{letter}\n")
            new_line = True
        elif letter == ' ' and new_line:
            continue
        else:
            print(letter, end="")
            new_line = False
