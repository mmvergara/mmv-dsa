class Solution:
    def hammingWeight(self, n: int) -> int:
        if n == 0:
            return n

        def rec(n, c=0):
            if n == 1:
                return c
            if n % 2 == 1:
                c += 1

            return rec(n // 2, c)

        return rec(n) + 1
