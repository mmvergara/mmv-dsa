def reverseBits(self, n: int) -> int:
    res = ""
    while n > 0:
        res += str(n % 2)
        n //= 2
    res += "0" * abs((len(res) - 32))
    return int(res, 2)
