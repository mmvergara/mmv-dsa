from randoms.dsa import *


# use dfs to count island
class Solution:
    def numIslands(self, matrix: List[List[str]]) -> int:
        visited = set()

        def dfs(r, c):
            # check if in bounds
            if r < 0 or r >= len(matrix) or c < 0 or c >= len(matrix[0]):
                return 0
            # check if visited and if it's a water
            if (r, c) in visited or matrix[r][c] == "0":
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
                if (r, c) in visited or matrix[r][c] == "0":
                    continue
                dfs(r, c)
                totalIslands += 1

        print(totalIslands)
        return totalIslands
