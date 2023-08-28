from dsa import *

class NumArray:

    def __init__(self, nums: List[int]):
        n = len(nums)
        self.arr = [0] * (n+1)
        for i in range(n):
            self.arr[i+1] = self.arr[i] + nums[i]
        

    def sumRange(self, left: int, right: int) -> int:
        return self.arr[right+1] - self.arr[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)