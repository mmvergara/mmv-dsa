import math

def countAnagrams(self, strr: str) -> int:
    def countCombs(s):
        hset = {}
        for x in s:
            if x in hset:
                hset[x] += 1
            else:
                hset[x] = 1
        combs = 1
        for c in hset.values():
            combs *= math.factorial(c)
        return math.factorial(len(s)) / combs

    def multiply(iterable):
        result = 1
        for num in iterable:
            result *= num
        return result

    return (int(sum([countCombs(x) for x in strr.split(" ")])) * len(strr)) % (10**9 + 7)


print(countAnagrams("", "aa"))
