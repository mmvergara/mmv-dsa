from dsa import *


def shuffle(self, nums: List[int], n: int) -> List[int]:
    ans = [None for _ in range(n * 2)]
    x = 0
    y = n
    for i in range(n * 2):
        if i % 2 == 0:
            ans[i] = nums[x]
            x += 1
        else:
            ans[i] = nums[y]
            y += 1
    print(ans)
    return ans


shuffle("", nums=[2, 5, 1, 3, 4, 7], n=3)
