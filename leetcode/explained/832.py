from dsa import *

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        for r in range(n):
            newR = [0] * n
            for c in range(n):
                newR[n-c-1] = image[r][c] ^ 1
            image[r] = newR

        return image


