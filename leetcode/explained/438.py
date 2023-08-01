from dsa import *

def findAnagrams(self, s: str, p: str) -> List[int]:
    # sliding window approach - compare frequency map in each window slide
    if len(p) > len(s):
        return []
    ast = {}
    curSt = {}
    ans = []

    for i in range(len(p)):
        if p[i] in ast:
            ast[p[i]]+=1
        else:
            ast[p[i]]=1

    
    l = r = 0
    
    curSt = {}
    while r < len(s):
        if r < len(p):
            if s[r] in curSt:
                curSt[s[r]]+=1
            else:
                curSt[s[r]]=1
            r+=1
            if curSt == ast:
                ans.append(0)
            continue
        
        if s[l] in curSt:
            curSt[s[l]]-=1
            if curSt[s[l]] == 0:
                del curSt[s[l]]
        if s[r] in curSt:
            curSt[s[r]]+=1
        else:
            curSt[s[r]]=1
        
        l+=1
        r+=1
        
        if curSt == ast:
            ans.append(l)

    print(ans)
    return ans



    


findAnagrams("",s = "cbaebabacd", p = "abc")
