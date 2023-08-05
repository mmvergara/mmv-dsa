from dsa import *


# learned, with fixed n combinations of an array, we can just use a for loop
def largestTriangleArea(self, points: List[List[int]]) -> float:
    def triangle_area(x1, y1, x2, y2, x3, y3):
        return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)

    max_area = 0
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            for k in range(j + 1, len(points)):
                print(
                    [
                        [points[i][0], points[i][1]],
                        [points[j][0], points[j][1]],
                        [points[k][0], points[k][1]],
                    ]
                )
                area = triangle_area(
                    points[i][0],
                    points[i][1],
                    points[j][0],
                    points[j][1],
                    points[k][0],
                    points[k][1],
                )
                if area > max_area:
                    max_area = area
    return max_area


largestTriangleArea("", [[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]])


[
    [[0, 0], [0, 1], [1, 0]],
    [[0, 0], [0, 1], [0, 2]],
    [[0, 0], [0, 1], [2, 0]],
    [[0, 0], [1, 0], [0, 2]],
    [[0, 0], [1, 0], [2, 0]],
    [[0, 0], [0, 2], [2, 0]],
    [[0, 1], [1, 0], [0, 2]],
    [[0, 1], [1, 0], [2, 0]],
    [[0, 1], [0, 2], [2, 0]],
    [[1, 0], [0, 2], [2, 0]],
]


# MY SOLUTION
# class Solution:
#     def largestTriangleArea(self, points: List[List[int]]) -> float:
#         # generate all combs
#         combs = []

#         def rec(combs, i=0, comb=[]):
#             if len(comb) == 3:
#                 combs.append(comb[:])
#                 return
#             if i == len(points):
#                 return

#             rec(combs, i + 1, comb[:] + [points[i]])
#             rec(combs, i + 1, comb[:])

#         rec(combs)

#         # get the area of each triangle while keeping tract of the max
#         def triangle_area(x1, y1, x2, y2, x3, y3):
#             return 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))

#         maxArea = float("-inf")
#         for comb in combs:
#             x1, y1 = comb[0]
#             x2, y2 = comb[1]
#             x3, y3 = comb[2]
#             maxArea = max(triangle_area(x1, y1, x2, y2, x3, y3), maxArea)
#         return maxArea
