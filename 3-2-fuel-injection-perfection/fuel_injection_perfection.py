#!/usr/bin/env python2


def answer(n):
    n = int(n)
    i = 0
    while n > 1:
        if n & 1 ^ 1:
            n >>= 1
        else:
            n += 1 if n & 2 and n > 3 else -1
        i += 1
    return i


print(answer("4"))
print(answer("15"))
