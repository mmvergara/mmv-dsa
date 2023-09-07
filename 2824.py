class Solution:
    def minimumSum(self, num: int) -> int:
        x = sorted([int(x) for x in str(num)])
        return ((x[0] * 10) + x[2]) + ((x[1] * 10)+x[3])
        