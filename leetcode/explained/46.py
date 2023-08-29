from randoms.dsa import *

def permute(self, nums: List[int]) -> List[List[int]]:
    perms = []
    def dfs(arr,used=set()):
        print(arr)
        if len(arr) == len(nums):
            perms.append(arr)
            return
        for i in range(len(nums)):
            if nums[i] not in used:
                dfs([*arr,nums[i]],set([*used,nums[i]]))
    dfs([])
    return perms




permute("",[1,2,3])
