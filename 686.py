class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        c = a
        repeat = 1
        if b in a:
            return 1
        while b not in a:
            if len(a) > len(c) * 3 and len(a) > len(b):
                return -1
            a += c
            repeat += 1

        return repeat
