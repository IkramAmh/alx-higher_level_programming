#!/usr/bin/python3
def pow(a, b):
    c = a
    if b == 0:
        return 1
    elif b < 0:
        for i in range((-b) - 1):
            c = float(1 / (c * a))
    else:
        for i in range(b - 1):
            c = c * a
    return (c)
