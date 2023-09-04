def hammingDistance(self, x: int, y: int) -> int:
    res = 0
    xa = []
    ya = []

    while x > 0:
        xa.append(x % 2)
        x //= 2

    while y > 0:
        ya.append(y % 2)
        y //= 2

    if len(xa) < len(ya):
        xa += [0] * len(ya)

    if len(ya) < len(xa):
        ya += [0] * len(xa)

    for i in range(len(xa)):
        if xa[i] != ya[i]:
            res += 1
    return res


print(hammingDistance("", 1, 4))
