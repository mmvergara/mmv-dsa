from collections import deque


def has_exit(maze):
    print(maze)
    ROWS = len(maze)
    COLS = len(maze[0])

    # find k
    k = None
    found = False
    for r in range(ROWS):
        for c in range(COLS):
            if "k" in maze[r][c]:
                print("FOUND K")
                if k is None:
                    k = (r, c)
                    print("ADD K")
                else:
                    raise "There should be no multiple K"
    # Perform dfs starting from k

    # initialize four directions for bfs
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # initialize queue
    q = deque([k])

    # set of visited paths so we don't repeat
    visitedPaths = set([(k[0], k[1])])

    hasExit = False

    while q:
        r, c = q.popleft()

        # if is in the border
        if r == 0 or c == 0 or c == COLS - 1 or r == ROWS - 1:
            print(r,c)
            print(r == 0, c == 0, c == COLS - 1, r == ROWS - 1)
            hasExit = True
            break

        for dx, dy in directions:
            nr = r + dx
            nc = c + dy
            newLoc = (nr, nc)

            if newLoc not in visitedPaths and maze[newLoc[0]][newLoc[1]] != "#":
                q.append(newLoc)
                visitedPaths.add(newLoc)
    return hasExit



maze = [
    "########",
    "# # ####",
    "# #k#   ",
    "# # # ##",
    "# # # ##",
    "#      #",
    "########",
]

print(has_exit(maze))
