# https://leetcode.com/problems/sign-of-the-product-of-an-array/

def arraySign(self, nums: list[int]) -> int:
    prod = 1
    for n in nums:
        prod*=n
    
    if prod == 0:
        return 0
    if prod > 0:
        return 1
    if prod < 0:
        return -1

    