from dsa import *
import collections

def uniqueOccurrences(self, arr: List[int]) -> bool:
    c = collections.Counter(arr).values()
    return len(c) == len(set(c))


uniqueOccurrences("", [1, 2, 2, 1, 1, 3])
