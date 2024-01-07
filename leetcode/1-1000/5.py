class Solution:
    def longestPalindrome(self, s: str) -> str:
        # loop through
        # expand outward
        res = ""

        for i in range(len(s)):
            l = i
            r = i
            curStr = s[i]
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if l != r:
                    curStr = s[l] + curStr + s[r]
                r += 1
                l -= 1
            if len(curStr) > len(res):
                res = curStr

            l = i
            r = i + 1
            if r == len(s):
                continue
            curStr = ""
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if l != r:
                    curStr = s[l] + curStr + s[r]
                r += 1
                l -= 1
            if len(curStr) > len(res):
                res = curStr
        return res
