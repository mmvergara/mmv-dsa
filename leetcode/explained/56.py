from randoms.dsa import *


def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    intervals = sorted(intervals)
    print(intervals)
    if len(intervals) <= 1:
        return intervals

    res = []
    last = None
    for i in range(len(intervals)):
        current = intervals[i]
        if last is None:
            last = current
            continue

        if current[0] <= last[1]:
            last = [last[0], max(current[1], last[1])]
            continue
        else:
            res.append(last)
            last = current
    if last:
        res.append(last)

    return res


print(merge("", [[1, 4], [2, 3]]))
