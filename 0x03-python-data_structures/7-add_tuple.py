#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    _tuple_a = [0, 0]
    _tuple_b = [0, 0]
    for i in range(2):
        if ((len(tuple_a) - 1) >= i):
            _tuple_a[i] = tuple_a[i]
        if ((len(tuple_b) - 1) >= i):
            _tuple_b[i] = tuple_b[i]
    sum_1 = _tuple_a[0] + _tuple_b[0]
    sum_2 = _tuple_a[1] + _tuple_b[1]
    _sum = (sum_1, sum_2)
    return (_sum)
