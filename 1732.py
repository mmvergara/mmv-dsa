from dsa import *

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = 0
        cur = 0 

        for a in gain:
            cur += a
            ans = max(ans,cur)

        return ans
