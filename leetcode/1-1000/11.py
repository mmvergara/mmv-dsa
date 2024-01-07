from typing import List


class Solution:
    def maxArea(self, arr: List[int]) -> int:
        l = 0
        r = len(arr) - 1
        res = 0

        while l < r:
            # get the container area then apply to res

            res = max(min(arr[l], arr[r]) * (r - l), res)

            if arr[l] > arr[r]:
                r -= 1
            else:
                l -= 1

        return res


class Solution:
    def maxArea(self, arr: List[int]) -> int:
        l = 0
        r = len(arr) - 1
        res = 0

        while l < r:
            # get the container area then apply to res

            res = max(min(arr[l], arr[r]) * (r - l), res)

            if arr[l] > arr[r]:
                r -= 1
            else:
                l += 1

        return res
