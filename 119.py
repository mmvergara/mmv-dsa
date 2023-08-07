import math
from dsa import *

# C(n, k) = n! / (k! * (n - k)!), 
def getRow(self, n: int) -> List[int]:
    res = []
    for i in range(n + 1):
        res.append(
            math.trunc(math.factorial(n) / (math.factorial(i) * math.factorial(n - i)))
        )
    return res


getRow("", 4)
