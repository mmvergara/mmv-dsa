class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # sliding window approach - compare frequency map in each window slide
        # p = s1
        # s = s2
        if len(s1) > len(s2):
            return []
        ast = {}
        curSt = {}
        ans = []

        for i in range(len(s1)):
            if s1[i] in ast:
                ast[s1[i]] += 1
            else:
                ast[s1[i]] = 1

        l = r = 0

        curSt = {}
        while r < len(s2):
            if r < len(s1):
                if s2[r] in curSt:
                    curSt[s2[r]] += 1
                else:
                    curSt[s2[r]] = 1
                r += 1
                if curSt == ast:
                    return True
                continue

            if s2[l] in curSt:
                curSt[s2[l]] -= 1
                if curSt[s2[l]] == 0:
                    del curSt[s2[l]]
            if s2[r] in curSt:
                curSt[s2[r]] += 1
            else:
                curSt[s2[r]] = 1

            l += 1
            r += 1
            print(curSt, ast)
            if curSt == ast:
                return True

        return False
