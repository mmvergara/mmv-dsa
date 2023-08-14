class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        mp = {}
        for n in arr:   
            if n in mp:
                mp[n]+=1
            else:
                mp[n]=1


        for k,v in mp.items()
            if k != v:
                return False
        return True

