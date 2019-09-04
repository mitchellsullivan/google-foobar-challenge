#!/usr/bin/env python2
from fractions import Fraction, gcd


def identity_matrix(X):
    return ([[1 if i == j else 0 for i, c in enumerate(r)]
        for j, r in enumerate(X)])


def answer(m):
    h = len(m)
    if h == 1:
        return [1, 1]
    w = len(m[0])
    trans = [t for t in enumerate(m) if sum(t[1])]
    terms = [t for t in enumerate(m) if not sum(t[1])]
    lt = len(terms)

    for i, t in enumerate(terms):
        t[1][i] = 1

    for i, tRow in enumerate(trans):
        temp = [0] * w
        for j, row in enumerate(terms + trans):
            temp[j] = tRow[1][row[0]]
        trans[i] = (tRow[0], temp[:])

    m = terms + trans

    for i, r in enumerate(m):
        sumRow = sum(r[1])
        for j, cell in enumerate(r[1]):
            m[i][1][j] = Fraction(cell, sumRow)

    I = [m[i][1][:lt] for i in range(lt)]
    R = [m[i][1][:lt] for i in range(lt, h)]
    O = [m[i][1][lt:w] for i in range(lt)]
    Q = [m[i][1][lt:w] for i in range(lt, h)]
    IofQ = identity_matrix(Q)

    for i in range(len(Q)):
        for j in range(len(Q[0])):
            IofQ[i][j] -= Q[i][j]

    F = [row[:] for row in IofQ]
    h = len(F)
    I = identity_matrix(F)
    F = [F[i] + I[i] for i in range(h)]

    for i in range(h):
        F[i] = [x / F[i][i] for x in F[i]]
        for j in range(h):
            if j != i:
                r = [F[j][i] * x for x in F[i]]
                F[j] = [F[j][k] - x for k, x in enumerate(r)]

    F = [F[i][h:len(F[i])] for i in range(h)]
    w = len(R[0])
    FR = [[0 for i in range(w)] for j in range(h)]

    for i in range(h):
        for j in range(w):
            for k in range(len(R)):
                FR[i][j] += F[i][k] * R[k][j]

    denom = reduce(gcd, FR[0]) ** -1
    res = map(lambda x: denom * x, FR[0]) + [denom]

    return map(int, [res[0]] + filter(bool, res[1:]))


t1 = [
    [0, 2, 1, 0, 0],
    [0, 0, 0, 3, 4],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]
a1 = [7, 6, 8, 21]
 
t2 = [
    [0, 1, 0, 0, 0, 1],
    [4, 0, 0, 3, 2, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
a2 = [0, 3, 2, 9, 14]

print(answer(t1))
print(answer(t2))