class Solution:
    def areOccurrencesEqual(self, st: str) -> bool:
        mp = {}
        maxO = 0
        for s in st:
            if s in mp:
                mp[s]+=1
            else:
                mp[s]=1
            maxO = max(maxO,mp[s])

        return all([maxO == x for x in mp.values()])
        
        
        



