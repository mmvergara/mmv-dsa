from dsa import *


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)
        res = [None] * n
        mp = {}
        for i in range(n):
            mp[heights[i]] = names[i]

        sHeights = sorted(heights, reverse=True)
        for i in range(n):
            res[i] = mp[sHeights[i]]
        return res
