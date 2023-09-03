import sys


# Average salary ( highest and lowest salary excluded)
def average(self, salary: list[int]) -> float:
    highest = 0
    totalSum = 0
    lowest = sys.maxsize
    for s in salary:
        highest = max(s, highest)
        lowest = min(s, lowest)
        totalSum += s
    return (totalSum - lowest - highest) / (len(salary) - 2)


print(average("", [1000, 2000, 3000]))
