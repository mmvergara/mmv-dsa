def find_factors(num:int):
    factors = []
    for i in range(num):
        s = num % (i+1)
        if s == 0:
            factors.append(i+1)
    for i in range(len(factors)):
        factors[i] = factors[i] * factors[i]
    return factors


print(find_factors(24))
