#!/usr/bin/env python2
from itertools import permutations as perms


def answer(times, time_limit):
    n = len(times)
    bunns = range(n - 2)

    if not bunns:
        return []

    # Floyd-Warshall
    dist = times[:]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    # Infinite negative cycle? Yes if neg. in diag.
    if [r[i] for i, r in enumerate(dist) if r[i] < 0]:
        return bunns

    # Power set
    P = reduce(lambda z, x: z + [y + [x] for y in z], bunns, [[]])

    # Check all permutations of all subsets
    res = []

    for s in [list(p) for sub in P for p in perms(sub)]:
        # Begin at Start with 0 time
        current_spot = t = 0

        # Visit spots with these bunnies
        for bunny_spot in [b + 1 for b in s]:
            t += dist[current_spot][bunny_spot]
            current_spot = bunny_spot

        # Go to Bulkhead from last bunny
        t += dist[current_spot][n - 1]

        if t <= time_limit and len(res) < len(s):
            res = sorted(s)

        # Quit checking permutations of all bunnies
        if len(res) == n - 2:
            return res

    return res


times1 = [
	[0, 1, 1, 1, 1],
	[1, 0, 1, 1, 1],
	[1, 1, 0, 1, 1],
	[1, 1, 1, 0, 1],
	[1, 1, 1, 1, 0]
]
time_limit1 = 3

times2 = [
	[0, 2, 2, 2, -1],
	[9, 0, 2, 2, -1],
	[9, 3, 0, 2, -1],
	[9, 3, 2, 0, -1],
	[9, 3, 2, 2, 0]
]
time_limit2 = 1

print(answer(times1, time_limit1))
print(answer(times2, time_limit2))