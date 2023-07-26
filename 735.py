from dsa import *


def asteroidCollision(self, ast: List[int]) -> List[int]:
    def isOnCollision(left, right):
        sameSign = (left >= 0 and right >= 0) or (left < 0 and right < 0)
        leftGoingRight = left > 0
        rightGoingLeft = right < 0
        return (not sameSign) and leftGoingRight and rightGoingLeft

    if len(ast) <= 1:
        return ast

    stack = []

    for i in range(len(ast)):
        stack.append(ast[i])
        print(stack)
        # while on collision
        while len(stack) >= 2 and isOnCollision(stack[-2], stack[-1]):
            # if same value pop both
            if abs(stack[-2]) == abs(stack[-1]):
                stack.pop()
                stack.pop()
                continue

            if abs(stack[-1]) > abs(stack[-2]):
                top = stack.pop()
                stack.pop()
                stack.append(top)
            else:
                stack.pop()
    return stack


asteroidCollision("", [-2, 2, 1, -2])
# asteroidCollision("", [-2, -1, 1, -2])
