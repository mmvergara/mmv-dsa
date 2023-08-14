class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        mp = {}
        for n in nums:
            if n in mp:
                mp[n]+=1
            else:
                mp[n]=1
        
        pairs = lo = 0
        for k,v in mp.items():
            pairs+=math.trunc(v / 2)
            lo+=round(v%2)


        return [pairs,lo]



