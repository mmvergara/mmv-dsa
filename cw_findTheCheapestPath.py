import sys


def cheapest_path(t, start, finish):
    ROWS = len(t)
    COLS = len(t[0])

    paths = []

    directions = [
        (0, -1),
        (-1, 0),
        (1, 0),
        (0, 1),
    ]

    def dfs(r, c, curPath: list):
        path = curPath.copy()
        path.append((r, c))
        if (r, c) == finish:
            paths.append(path)

        for dx, dy in directions:
            new_r = r + dx
            new_c = c + dy

            if 0 <= new_r < ROWS and 0 <= new_c < COLS and (new_r, new_c) not in path:
                dfs(new_r, new_c, path)

    dfs(start[0], start[1], [])

    cheapestI = 0
    cheapestT = sys.maxsize
    for i in range(len(paths)):
        total = sum([t[r][c] for r, c in paths[i]])
        if total < cheapestT:
            cheapestT = total
            cheapestI = i

    coordinates = paths[cheapestI]
    dirs = []

    for i in range(len(coordinates) - 1):
        x1, y1 = coordinates[i]
        x2, y2 = coordinates[i + 1]

        if (x1 + 1, y1) == (x2, y2):
            dirs.append("down")
        elif (x1, y1 + 1) == (x2, y2):
            dirs.append("right")
        elif (x1, y1 - 1) == (x2, y2):
            dirs.append("left")
        else:
            dirs.append("up")

    return dirs


cheapest_path([[1, 9, 1], [2, 9, 1], [2, 1, 1]], (0, 0), (0, 2))
