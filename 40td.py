class Solution:

    def combinationSum2(self,candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        subsets = []

        def backtrack(start, target_left, current_subset):
            if target_left == 0:
                subsets.append(current_subset)
                return

            for i in range(start, len(candidates)):
                # Skip duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                if candidates[i] > target_left:
                    break
                
                backtrack(i + 1, target_left - candidates[i], current_subset + [candidates[i]])

        backtrack(0, target, [])
        return subsets

