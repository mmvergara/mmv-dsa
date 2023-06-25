from dsa import *
import math

# just binary search then find the target


def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
    def binaryMatrix(matrix, start, end, target):
        if end == None:
            end = len(matrix) - 1

        if start > end:
            return False

        mid = math.trunc((start + end) / 2)

        if target in matrix[mid]:
            return True

        # if we cannot find get the last element of the current middle array and deduce from there wether to go right or left
        if target > matrix[mid][-1]:
            return binaryMatrix(matrix, mid + 1, end, target)
        else:
            return binaryMatrix(matrix, start, mid - 1, target)

    return binaryMatrix(matrix, 0, None, target)


res = searchMatrix("", [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3111)
print(res)
