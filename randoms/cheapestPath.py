import heapq


def inBounds(r, c, rb, cb):
    return (0 <= r and r < rb) and (0 <= c and c < cb)


def cheapest_path(mat, start, finish):
    ROWS = len(mat)
    COLS = len(mat[0])
    directions = {
        "right": (0, 1),
        "left": (0, -1),
        "up": (-1, 0),
        "down": (1, 0),
    }
    visited = set()
    # loc : weight,lastDir
    dist = {start: (mat[start[0]][start[1]], None)}
    # (weight,loc,lastDir)
    queue = [(mat[start[0]][start[1]], start, None)]

    while queue:
        w, (r, c), lastDir = heapq.heappop(queue)

        if (r, c) == finish:
            break

        if (r, c) in visited:
            continue

        visited.add((r, c))

        for direction, (dx, dy) in directions.items():
            newR = r + dx
            newC = c + dy
            newLoc = (newR, newC)

            # check if inBounds
            if not inBounds(newR, newC, ROWS, COLS):
                continue

            # calc updated weight
            updatedWeight = w + mat[newR][newC]

            # relaxation
            if newLoc not in dist or dist[newLoc][0] > updatedWeight:
                dist[newLoc] = (updatedWeight, direction)

            # push to queue
            heapq.heappush(queue, (dist[newLoc][0], newLoc, direction))
    print(dist)


cheapest_path(
    [
        [1, 9, 1],
        [2, 9, 1],
        [2, 1, 1],
    ],
    (0, 0),
    (0, 2),
)


x = {
    (0, 0): (1, None),
    (0, 1): (10, "right"),
    (1, 0): (3, "down"),
    (1, 1): (12, "right"),
    (2, 0): (5, "down"),
    (2, 1): (6, "right"),
    (2, 2): (7, "right"),
    (1, 2): (8, "up"),
    (0, 2): (9, "up"),
}

x = {
    (0, 0): (1, None),
    (0, 1): (10, "right"),
    (1, 0): (3, "down"),
    (1, 1): (12, "right"),
    (2, 0): (5, "down"),
    (2, 1): (6, "right"),
    (2, 2): (7, "right"),
    (1, 2): (8, "up"),
    (0, 2): (9, "up"),
}
