

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mp = {}
        for l in magazine:
            if l in mp:
                mp[l]+=1
                continue
            mp[l] = 1
        
        for l in ransomNote:
            if l not in mp:
                return False

            mp[l]-=1
            if mp[l] < 0:
                return False

    
        return True

