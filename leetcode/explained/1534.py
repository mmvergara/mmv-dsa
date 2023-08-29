from randoms.dsa import *

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        count = 0
        for i in n:
            for j in n:
                for k in n:
                    if not (abs(arr[i] - arr[j]) <= a):
                        break

                    if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        count += 1

        return count
