from randoms.dsa import *


# perform dfs to count island area
class Solution:
    def maxAreaOfIsland(self, matrix: List[List[int]]) -> int:
        visited = set()

        def dfs(r, c):
            # check if in bounds
            if r < 0 or r >= len(matrix) or c < 0 or c >= len(matrix[0]):
                return 0
            # check if visited and if it's a water
            if (r, c) in visited or matrix[r][c] == 0:
                return 0
            visited.add((r, c))

            total = 1

            # move down
            total += dfs(r + 1, c)
            # move up
            total += dfs(r - 1, c)
            # move right
            total += dfs(r, c + 1)
            # move left
            total += dfs(r, c - 1)

            return total

        maxIsland = 0
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if (r, c) in visited or matrix[r][c] == 0:
                    continue
                maxIsland = max(dfs(r, c), maxIsland)

        return maxIsland
