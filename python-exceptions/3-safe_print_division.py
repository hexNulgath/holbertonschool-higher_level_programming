#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        if result is None:
            print("Inside result: None")
        else:
            print("Inside result: {:.2}".format(result))
        return result
