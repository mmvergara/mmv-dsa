import math


def loose_change(cents):
    cents = math.trunc(cents)

    res = {"Nickels": 0, "Pennies": 0, "Dimes": 0, "Quarters": 0}
    if cents < 0:
        return res
    coins = [("Quarters", 25), ("Dimes", 10), ("Nickels", 5), ("Pennies", 1)]
    total = 0
    coinI = 0

    while total != cents:
        if coins[coinI][1] + total <= cents:
            res[coins[coinI][0]] += 1
            total += coins[coinI][1]
            continue
        coinI += 1

    return res


loose_change(56)
