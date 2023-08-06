m = [
    ["W", "L", "W", "W", "L", "W"],
    ["L", "L", "W", "W", "L", "W"],
    ["W", "L", "W", "W", "W", "W"],
    ["W", "W", "W", "L", "L", "W"],
    ["W", "L", "W", "L", "L", "W"],
    ["W", "W", "W", "W", "W", "W"],
]


def islandCount(matrix) -> int:
    visited = set()

    def dfs(r, c):
        # check if in bounds
        if r < 0 or r >= len(matrix) or c < 0 or c >= len(matrix[0]):
            return 0
        # check if visited and if it's a water
        if (r, c) in visited or matrix[r][c] == "W":
            return
        visited.add((r, c))
        # move down
        dfs(r + 1, c)
        # move up
        dfs(r - 1, c)
        # move right
        dfs(r, c + 1)
        # move left
        dfs(r, c - 1)

    totalIslands = 0
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if (r, c) in visited or matrix[r][c] == "W":
                continue
            dfs(r, c)
            totalIslands += 1

    print(totalIslands)
    return totalIslands


islandCount(m)

[
    ["1", "0", "1", "1", "1"],
    ["1", "0", "1", "0", "1"],
    ["1", "1", "1", "0", "1"],
]
