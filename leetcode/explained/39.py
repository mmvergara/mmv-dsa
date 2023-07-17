from dsa import *

def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    res = []
    def gen(target, k, candidates, curCan):
        if target == 0:
            res.append(curCan[:])
        if target < 0:
            return
        for i in range(k, len(candidates)):
            remainder = target - candidates[i]
            gen(remainder, i, candidates, curCan + [candidates[i]])
    gen(target, 0, candidates, [])
    return res

print(combinationSum("", [2,3,5], 8))
