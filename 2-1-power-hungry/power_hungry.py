#!/usr/bin/env python2
from functools import reduce


def answer(xs):
    if len(xs) == 1:
        return str(xs[0])
    pos = list(filter(lambda x: x > 0, xs))
    neg = list(filter(lambda x: x < 0, xs))
    maxNeg = (sorted(neg, reverse=True)[0:] or [0])[0]
    product = (reduce(lambda x, y: x * y, pos + neg, 1)
               if pos or neg else 0)
    result = 0
    if product >= 0:
        result = product
    else:
        if maxNeg != product:
            result = product // maxNeg
    return str(result)

###

tests = [
    [2, 0, 2, 2, 0],
    [-2, -3, 4, -5],
]

for t in tests:
    print(answer(t))
