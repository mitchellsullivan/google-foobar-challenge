#!/usr/bin/env python2
from collections import deque


def edmonds_karp(net, s, t):
    l = len(net)
    # Create residual network as zero-matrix.
    res_net = [[0] * l for i in range(l)]
    # BFS to find shortest path from source, s, to terminal, t, with
    # available capacity.
    path = search(net, s, t, res_net)
    # Breaks when no path is returned from BFS.
    while path:
        # Find bottleneck.
        b = min([net[u][v] - res_net[u][v] for u, v in path])

        # Adjust edge in residual network, both directions.
        for u, v in path:
            res_net[u][v] += b
            res_net[v][u] -= b

        # Find path again.
        path = search(net, s, t, res_net)

    # Starting edges in residual network now represent most augmented paths.
    # Sum their flows.
    max_flow = sum(res_net[s][node] for node in range(l))

    return max_flow


def search(net, s, t, res):
    l = len(net)
    # "queue"
    q = deque([s])
    # Track visited nodes.
    vis = [0] * l
    # Accumulate edges for a given node represented by index.
    adj = [[] for i in range(l)]

    while q:
        u = q.popleft()

        for v in range(l):
            # If available capacity and neighbor is unvisited.
            if net[u][v] - res[u][v] and not vis[v]:
                # Visit
                vis[v] = 1
                # Add edge
                adj[v] = adj[u] + [[u, v]]
                q.append(v)

                # End found
                if v == t:
                    return adj[v]


def answer(entrances, exits, path):
    l = len(path)
    # Convert multiple entrances to one dummy entrance with all bunnies, and
    # multiple exits to one dummy exit with all escape pods. Keep square.
    bunny_room = [[0] * (l + 2)]
    pod_room = bunny_room[:]

    # Set capacities of dummy entrance -> original entrances to Infinity.
    for e in entrances:
        bunny_room[0][e + 1] = float("Inf")

    for p in path:
        # Bump existing values in path forward. Add index for new exit.
        p[:0] = [0]
        p.append(0)

    # Set capacities of original exits -> dummy exit to Infinity.
    for e in exits:
        path[e][l + 1] = float("Inf")

    # Create a single-source, single-sink matrix by concatenating the
    # previous portions.
    path[:0] = bunny_room
    path.append(pod_room)
    # Run Emdonds-Karp algorithm on new matrix.
    escapees = edmonds_karp(path, 0, l + 1)

    return escapees


en1 = [0]
ex1 = [3]
p1 = [
    [0, 7, 0, 0],
    [0, 0, 6, 0],
    [0, 0, 0, 8],
    [9, 0, 0, 0]
]
a1 = 6

en2 = [0, 1]
ex2 = [4, 5]
p2 = [
    [0, 0, 4, 6, 0, 0],
    [0, 0, 5, 2, 0, 0],
    [0, 0, 0, 0, 4, 4],
    [0, 0, 0, 0, 6, 6],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
a2 = 16

print(answer(en1, ex1, p1))
print(answer(en2, ex2, p2))
