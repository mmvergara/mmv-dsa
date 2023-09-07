class Solution:
    def isUgly(self, n: int) -> bool:
        if n < 1: return False
        
        # Handle the factor of 2
        while n % 2 == 0:
            n //= 2
        
        # Check for odd prime factors
        for i in [2,3,5]:
            while n % i == 0:
                n //= i

        return n == 1