class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        if s1 == s2:
            return True

        diffs = 0
        mp1 = {}
        mp2 = {}
        for i in range(len(s1)):
            a = s1[i]
            b = s2[i]
            if a in mp1:
                mp1[a] += 1
            else:
                mp1[a] = 1

            if b in mp2:
                mp2[b] += 1
            else:
                mp2[b] = 1
            if a != b:
                diffs += 1

        return diffs == 2 and mp1 == mp2
