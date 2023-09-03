def findComplement(self, num: int) -> int:
    x = 1
    res = 0
    while num > 0:
        bits = num % 2
        res += (bits ^ 1) * x
        x *= 2
        num //= 2
    return res


findComplement("", 5)
