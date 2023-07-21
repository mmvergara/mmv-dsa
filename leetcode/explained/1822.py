# https://leetcode.com/problems/sign-of-the-product-of-an-array/

def arraySign(self, nums: list[int]) -> int:
    prod = 1
    # get the prod
    for n in nums:
        prod*=n

    # 0 if prod is 
    # 1 if prod is positive
    # -1 if prod is negative

    if prod == 0:
        return 0
    if prod > 0:
        return 1
    if prod < 0:
        return -1

    