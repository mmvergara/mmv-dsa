from dsa import *

# we can deal with dup values with hashmaps
def arrayRankTransform(self, arr: List[int]) -> List[int]:
    sArr = sorted(arr)
    ranks = {sArr[0]: 1}

    for i in range(1, len(sArr)):
        if sArr[i] != sArr[i - 1]:
            ranks[sArr[i]] = ranks[sArr[i - 1]] + 1
    
    for i in range(len(arr)):
        arr[i] = ranks[arr[i]]

    return arr


arrayRankTransform("", [37, 12, 28, 9, 100, 56, 80, 5, 5, 12])
