def isBadVersion(x:int):
    return x > 3

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

def firstBadVersion(self, n: int) -> int:
    if n == 1: return 1
    left = 0 
    right = n+1
    while left+1 != right:
        mid = round((left+right)/2)
        midIsBad = isBadVersion(mid)
        if midIsBad and isBadVersion(mid-1) == False:
            return mid
        elif midIsBad:
            right = mid
        else:
            left = mid
    return None