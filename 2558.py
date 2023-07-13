from dsa import *
from math import floor, sqrt
from heapq import heapify


def pickGifts(gifts: List[int], k: int) -> int:
    h = [-g for g in gifts]
    heapify(h)

    for _ in range(k):
        if not h:
            return 0
        g = -heapq.heappop(h)
        sqr = floor(sqrt(g))
        heapq.heappush(h, -sqr)
        print(h)

    return -sum(h)


pickGifts([25, 64, 9, 4, 100], 4)
