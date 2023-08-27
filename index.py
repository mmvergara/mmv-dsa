import math
def primeFactors(n):
    res = set()
    # Print 2 as many times as it divides n
    while n % 2 == 0:
        res.add(2)
        n //= 2

    # Check for odd prime factors
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        
        # take i if we can still
        while n % i == 0:
            res.add(i)
            n //= i

    # If n is still greater than 2, it's a prime factor
    if n > 2:
        res.add(n)
    print(res)
    return res

# Driver program
n = 315
primeFactors(n)
