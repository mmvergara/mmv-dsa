
def numIdenticalPairs(self, nums: List[int]) -> int:
    mp = {}

    pairs = 0
    for i in range(len(nums)):
        if nums[i] in mp:
            pairs+=mp[nums[i]]
            mp[nums[i]]+=1
        else:
            mp[nums[i]]=1
            
    
    return pairs

