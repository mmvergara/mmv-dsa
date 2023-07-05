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
    # get the highest factor
    factors = get_factors(l, b)

    # then divide it to the product of the 2 grid size
    return math.trunc((l * b) / (factors[-1] * factors[-1]))
