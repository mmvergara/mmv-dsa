from dsa import *


def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
    # create a map of letters and their starting positions:

    startingPoints = {}
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] in startingPoints:
                startingPoints[board[r][c]].append((r, c))
            else:
                startingPoints[board[r][c]] = [(r, c)]

    valid = []


    pass


findWords(
    "",
    board=[
        ["o", "a", "a", "n"],
        ["e", "t", "a", "e"],
        ["i", "h", "k", "r"],
        ["i", "f", "l", "v"],
    ],
    words=["oath", "pea", "eat", "rain"],
)
