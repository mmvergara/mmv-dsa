class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        p = {}
        for a,b in paths:
            p[a] = b

        cur = paths[0][0]

        while cur in p:
            cur = p[cur]
        
        return cur



