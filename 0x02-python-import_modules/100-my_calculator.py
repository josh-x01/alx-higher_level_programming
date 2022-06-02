#!/usr/bin/python3
if (__name__ == "__main__"):
    from calculator_1 import add, sub, mul, div
    import sys
    arg = sys.argv
    _len = len(arg)
    operators = ["+", "-", "*", "/"]

    if (_len != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    elif (arg[2] not in operators):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    else:
        op = arg[2]
        a = int(arg[1])
        b = int(arg[3])

        if (op == "+"):
            print("{} {} {} = {}".format(a, op, b, add(a, b)))
        elif (op == "-"):
            print("{} {} {} = {}".format(a, op, b, sub(a, b)))
        elif (op == "*"):
            print("{} {} {} = {}".format(a, op, b, mul(a, b)))
        else:
            print("{} {} {} = {}".format(a, op, b, div(a, b)))
            sys.exit(1)
