from dsa import *


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        print(intervals, newInterval)

        def check_overlap(interval1, interval2):
            start1, end1 = interval1
            start2, end2 = interval2
            return max(start1, start2) <= min(end1, end2)

        def insert_new_interval(intervals, newInterval):
            i = 0
            while i < len(intervals) and intervals[i][0] < newInterval[1]:
                i += 1
            intervals.insert(i, newInterval)
            return intervals

        inc = []
        for i in range(len(intervals)):
            if check_overlap(intervals[i], newInterval):
                inc.append(i)

        if len(inc) == 0:
            insert_new_interval(intervals, newInterval)
        else:
            newInt = [
                min(intervals[inc[0]][0], newInterval[0]),
                max(intervals[inc[-1]][1], newInterval[1]),
            ]
            for i in reversed(inc):
                del intervals[i]
            insert_new_interval(intervals, newInt)

        return intervals
