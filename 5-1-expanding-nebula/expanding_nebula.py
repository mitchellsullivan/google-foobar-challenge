#!/usr/bin/env python2


def answer(g):
    h = len(g)
    w = len(g[0])
    # Transpose the input matrix
    g_t = [[g[j][i] for j in range(h)] for i in range(w)]
    # Change each row in transpose matrix from bools to 1 and 0's to a decimal
    # representation of the row's 1's and 0's.
    bool_int_f = lambda x, y: str(int(x)) + str(int(y))
    rows_dec = [int(reduce(bool_int_f, row), 2) for row in g_t]
    # Possible rows of a certain width that we can have in this transposed
    # matrix, represented as a decimal integer from a binary row cells
    possible_rows = range(2 ** (len(g_t[0]) + 1))
    # Need set for lookups. Checking a list is too slow.
    row_set = set(rows_dec)
    # State map
    lookup = {}
    # Mask to remove most significant bit. Ex., Input 1: Width 4 for previous
    # state. Need width 3 for current state, and 2^[needed width] or 2 ^ 3 or 8
    # or 0b1000, minus 1, becomes 0b0111; giving us 3-bits for 1-less width.
    mask = 2 ** h - 1
    # Generate pairings of possible rows
    for pr1 in possible_rows:
        # Don't repeat pairs in reverse order
        for pr2 in possible_rows[pr1:]:
            # Ditch the most significant bit and invert
            ntl = ~(pr1 & mask)
            nbl = ~(pr2 & mask)
            # Ditch least significant bit and invert
            ntr = ~(pr1 >> 1)
            nbr = ~(pr2 >> 1)
            # Revert one at a time
            ops = [
                ~ntl & nbl & ntr & nbr,
                ntl & ~nbl & ntr & nbr,
                ntl & nbl & ~ntr & nbr,
                ntl & nbl & ntr & ~nbr
            ]
            # Combine the 1's positions found
            result = ops[0] | ops[1] | ops[2] | ops[3]
            # If the resulting transition of these two possible rows from the
            # previous state is a row in the input, we've found a potential
            # pair of rows from the previous state.
            if result in row_set:
                # Add second row to first row's pairings for this result, or...
                if pr1 in lookup:
                    if result in lookup[pr1]:
                        lookup[pr1][result].add(pr2)
                    else:
                        lookup[pr1][result] = {pr2}
                # ... Add first row to state map if it hasn't been seen.
                else:
                    lookup[pr1] = {result: {pr2}}
                # Same as above, re-using results in reversed row order.
                if pr2 in lookup:
                    if result in lookup[pr2]:
                        lookup[pr2][result].add(pr1)
                    else:
                        lookup[pr2][result] = {pr1}
                else:
                    lookup[pr2] = {result: {pr1}}
    # Going to have current-next, passing-off situation. Will hold valid rows
    # and represent branching possibilities by accumulating nums of pairings.
    current = {}
    # Step through the decimal-represented rows in tranposed example input.
    for rdi in range(len(rows_dec)):
        # On first row prep counters at 1 for all possible rows as potential
        # starting rows; a dummmy.
        if rdi == 0:
            for r in possible_rows:
                current[r] = 1

        target = rows_dec[rdi]
        next = {}
        # Row is both currently valid and in state map
        intersect = current.viewkeys() & lookup.viewkeys()
        for row1 in intersect:
            # If we can get the current row of our current input state by the
            # transition function of this row with another row (otherwise it's a
            # dead-end)...
            if target in lookup[row1]:
                # ... then get the other rows by treating input row as the
                # result of pairings with row1
                for row2 in lookup[row1][target]:
                    # If carried over, accumulate the unique ways we could have
                    # gotten here.
                    if row2 in next:
                        next[row2] += current[row1]
                    else:
                        next[row2] = current[row1]

        # Abandon current set and move to the one that was just built. before
        # going to the next target row of the input.
        current = next
        # If on last row, sum accumulated possibilities; the number of "paths"
        # through the possibilities from the first input row to the last.
        if rdi == w - 1:
            result = 0
            for k in current:
                result += current[k]
            return result
    return 0


g1 = [
    [1, 0, 1],
    [0, 1, 0],
    [1, 0, 1]
]
a1 = 4

g2 = [
    [1, 0, 1, 0, 0, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 1, 0],
    [1, 1, 1, 0, 0, 0, 1, 0],
    [1, 0, 1, 0, 0, 0, 1, 0],
    [1, 0, 1, 0, 0, 1, 1, 1]
]
a2 = 254

g3 = [
    [1, 1, 0, 1, 0, 1, 0, 1, 1, 0],
    [1, 1, 0, 0, 0, 0, 1, 1, 1, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 0, 1, 1, 0, 0]
]
a3 = 11567


print(answer(g1))
print(answer(g2))
print(answer(g3))