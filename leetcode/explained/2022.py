from dsa import *


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        # check if it's possible
        if len(original) != (m * n):
            return []

        ans = [[None for _ in range(n)] for _ in range(m)]

        for r in range(m):
            for c in range(n):
                ans[r][c] = original[((r * n) + c)]

        return ans
