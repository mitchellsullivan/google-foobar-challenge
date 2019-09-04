#!/usr/bin/env python2


def toBase(n, b):
    dig = "0123456789"
    quo, rem = divmod(n, b)
    return dig[n] if n < b else toBase(quo, b) + dig[rem]

def answer(n, b):
    cycle = []
    while 1:
        y = "".join(sorted(str(n)))
        x = "".join(reversed(y))
        z = toBase(int(x, b) - int(y, b), b)
        for i, elem in enumerate(cycle):
            if elem == z:
                return i + 1
        cycle[:0] = [z]
        n = z


print(answer(1211, 10))
print(answer(210022, 3))