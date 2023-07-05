import math

def get_factors(num1, num2):
    factors = []
    for i in range(1, min(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            factors.append(i)
    return factors

def restaurant(l, b):
    if l == b:
        return 1
    x = get_factors(l,b)
    return math.trunc((l*b)/(x[-1] * x[-1]))
    