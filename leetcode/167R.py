from dsa import *

# Two sum but with a sorted array, initialize right and left pointer
# increment left pointer to increase the sum if sum < target
# decrement right pointer to decrease the sum if sum > target

def twoSum(self, numbers: List[int], target: int) -> List[int]:
    i = 0
    j = len(numbers) - 1

    while i <= j:
        total = numbers[i] + numbers[j]
        if total == target:
            return [i + 1, j + 1]
        if total > target:
            j -= 1
        else:
            i += 1
    return []
