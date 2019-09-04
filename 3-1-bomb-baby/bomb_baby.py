#!/usr/bin/python


def answer(M, F):
    lo, hi = sorted(map(int, [M, F]))
    i = -1
    while lo > 1:
        hi, lo, i = lo, hi % lo, hi // lo + i
    return str(i + hi) if lo else "impossible"


print(answer("1", "2"))
print(answer("4", "7"))