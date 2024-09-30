#!/usr/bin/python3
"""
This module allows for appending command-line arguments to a JSON file.
It uses functions to load a Python object from a JSON file and save a Python
object to a JSON file.
"""

import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


def main():
    """
    Main function that loads arguments from the command line, appends them
    to an existing list (if present) in a JSON file, and then saves the
    updated list back to the JSON file.

    - Loads existing data from 'add_item.json', if available.
    - Appends command-line arguments (excluding the script name).
    - Saves the updated list of arguments back to 'add_item.json'.

    Args:
        None (Uses sys.argv for input).

    Raises:
        FileNotFoundError: If 'add_item.json' is not found, an empty list is
                           initialized.
    """
    destination = "add_item.json"

    try:
        # Try to load the existing data from the JSON file
        data = load_from_json_file(destination)
    except FileNotFoundError:
        # If the file doesn't exist, start with an empty list
        data = []

    # Append new arguments from the command line (excluding the script name)
    data.extend(sys.argv[1:])

    # Save the updated list back to the JSON file
    save_to_json_file(data, destination)


if __name__ == "__main__":
    main()
