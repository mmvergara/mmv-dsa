import numpy as np
import matplotlib.pyplot as plt

# a = m^2 - n^2
# b = 2mn
# c = m^2 + n^2


def gen():
    numberRange = np.arange(2, 51)
    res = {"a": [], "b": [], "c": []}
    for m in numberRange:
        for n in numberRange:
            if m < n:
                continue
            a = (m**2) - (n**2)
            b = 2 * m * n
            c = (m**m) + (n**n)
            res["a"].append(a)
            res["b"].append(b)
            res["c"].append(c)
    print(res)
    return res


res = gen()

plt.plot(res["a"], res["b"], 0)
