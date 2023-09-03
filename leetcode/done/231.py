class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Base Cases
        if n == 1:
            return True
        if n % 2 != 0:
            return False
        
        while n > 2:
            if n % 2 != 0:
                return False
            n = n // 2
        
        return n == 2