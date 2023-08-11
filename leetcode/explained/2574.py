from dsa import *

    def leftRightDifference(self, nums: List[int]) -> List[int]:
    N = len(nums)
    ans = [0 for _ in range(N)]

    # get left sum
    ls = 0 
    for i in range(N-1):
        ls += nums[i]
        ans[i+1]= ls

    # get right sum
    rs = 0
    for i in range(N-1,0,-1):
        rs += nums[i]
        ans[i-1] = abs(rs-ans[i-1])
    print(ans)
    return ans



leftRightDifference("",[10,4,8,3])


