#!/usr/bin/python3
def safe_print_division(a, b):
    result = 0
    try:
        result = a / b
        print("Inside result: {}".format(result))
    except ZeroDivisionError:
        return None
    finally:
        print("{:.1f}".format(result))
    return result
