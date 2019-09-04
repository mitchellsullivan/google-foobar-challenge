#!/usr/bin/env python2
import math

def answer(area):
    panels = []
    if area >= 0 and area <= 1000000:
        while area > 0:
            maxSqr = maxSquareLessThan(area);
            panels.append(maxSqr)
            area -= maxSqr
    return panels

def maxSquareLessThan(i):
    intSqrt = int(math.sqrt(i))
    return int(math.pow(intSqrt, 2))

print(answer(999999))

