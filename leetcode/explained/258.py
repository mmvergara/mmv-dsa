class Solution:
    def addDigits(self, num: int) -> int:

        def rec(n):
            if n < 10:
                return n
            return n//10 + rec(n%10)

        while num > 9:
            num = rec(num)

        return num