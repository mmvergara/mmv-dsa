def gridTraveler(m, n):
    grid = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    grid[1][1] = 1

    for r in range(1, len(grid)):
        for c in range(1, len(grid)):
            if r == 1 and c == 1:
                continue
            grid[r][c] = grid[r - 1][c] + grid[r][c - 1]

    print(grid[-1][-1])
    


gridTraveler(18, 18)
