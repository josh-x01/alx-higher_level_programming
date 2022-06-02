#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    from calculator_1 import add, sub, mul, div

    op_fun = [
        ["+", add],
        ["-", sub],
        ["*", mul],
        ["/", div]
    ]
    i = 0

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        a = int(sys.argv[1])
        op = sys.argv[2]
        b = int(sys.argv[3])

        while i < len(op_fun):
            if op == op_fun[i][0]:
                execute = op_fun[i][1](a, b)
                print('{:d} {} {:d} = {:d}'.format(a, op, b, execute))
                sys.exit(0)
            i += 1
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
