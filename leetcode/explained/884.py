from randoms.dsa import *

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        arr1 = s1.split(" ")
        arr2 = s2.split(" ")
        mp = {}

        for s in arr1:
            if s in mp:
                mp[s] += 1
            else:
                mp[s] = 1

        for s in arr2:
            if s in mp:
                mp[s] += 1
            else:
                mp[s] = 1
        res = []
        for k,v in mp.items():
            if v == 1:
                res.append(k)

        return res




        
