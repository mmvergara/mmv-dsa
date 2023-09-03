class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mp = {}
        arr = s.split(" ")

        for i in range(len(pattern)):
            c = pattern[i]
            if c not in mp:
                mp[c] = arr[i]
            else:
                if mp[c] != arr[i]:
                    return False

        return True

