
def maxSubArray(self, nums: list[int]) -> int:
    total = 0
    highest = float('-inf')
    for n in nums:
        total = max(n,total+n)
        highest = max(total,highest)

    return highest



