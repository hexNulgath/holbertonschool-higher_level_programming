#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, div, mul
    import sys

    argv = sys.argv[1:]
    argc = len(argv)

    if argc != 3:
        print(f"Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(argv[0])
    operator = argv[1]
    b = int(argv[2])

    if operator == '+':
        print(f"{a} + {b} = {add(a, b)}")
    elif operator == '-':
        print(f"{a} - {b} = {sub(a, b)}")
    elif operator == '*':
        print(f"{a} * {b} = {mul(a, b)}")
    elif operator == '/':
        print(f"{a} / {b} = {div(a, b)}")
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
