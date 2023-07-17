import heapq
from collections import deque
# AGHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH

def inBounds(r, c, rb, cb):
    return (0 <= r and r < rb) and (0 <= c and c < cb)


def cheapest_path(t, start, finish):
    ROWS = len(t)
    COLS = len(t[0])
    #

    directions = {
        "right": (0, 1),
        "left": (0, -1),
        "up": (-1, 0),
        "down": (1, 0),
    }

    rev = {"right": "left", "left": "right", "up": "down", "down": "up"}
    visited = set()
    dist = {start: (t[start[0]][start[1]], None)}
    queue = [(t[start[0]][start[1]], start, None)]

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
            if inBounds(newR, newC, ROWS, COLS):
                updatedWeight = t[newR][newC] + w
                if newLoc not in dist or dist[newLoc][0] > updatedWeight:
                    dist[newLoc] = (updatedWeight, direction)
                heapq.heappush(queue, (dist[newLoc][0], newLoc, direction))

    curLoc = finish
    path = deque()
    while dist[curLoc][1] is not None:
        _, d = dist[curLoc]
        path.appendleft(d)
        dx, dy = directions[rev[d]]
        curLoc = (dx + curLoc[0], dy + curLoc[1])

    return list(path)


cheapest_path([[1, 9, 1], [2, 9, 1], [2, 1, 1]], (0, 0), (0, 2))
