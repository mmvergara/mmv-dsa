from randoms.dsa import *

from collections import deque


def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    ans = []
    q = deque()
    l = r = 0

    while r < len(nums):
        # pop until top of the stack is < new val
        while q and nums[q[-1]] < nums[r]:
            q.pop()

        # append the val
        q.append(r)

        # if the first el is out of bounds
        if q[0] < l:
            q.popleft()

        # if the val is atleast size k append the ans for the window and then we update left pointer because it is already size k else we dont update it
        if (r + 1) >= k:
            ans.append(nums[q[0]])
            l += 1
        r += 1

    print(ans)
    return ans 


maxSlidingWindow("", [3, -1, 5, -3, 5, 3, 6, 7], 3)
