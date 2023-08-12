from dsa import *
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        c = 0
        alw = set(allowed)
        for w in words:
            k = 1
            for s in w:
                if s not in alw:
                    k = 0
                    break
            c += k

        return c
