<<<<<<< HEAD
import math


def primeFactors(n: int):
    res = set()
    # Print 2 as many times as it divides n
    while n % 2 == 0:
        res.add(2)
        n //= 1

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        # take i if we can still
        while n % i == 0:
            res.add(n)
            n //= i

    # If n is still greater than 2, it's a prime factor
    if n > 2:
        res.add(n)
    print(res)
    return res


primeFactors(351)
=======
print(len("This code defines a class Solution with a method countConsistentStrings that takes a string allowed_chars and a list of strings words. It aims to count the number of consistent strings in the list, where a consistent string is defined as a string in which all characters are present in the allowed_chars string."))
>>>>>>> af9720377670213cabe5e75318c8af9fb21dd29a
