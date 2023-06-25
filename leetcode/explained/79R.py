# We are usin dfs, first of all find the locations where the val is == to the first letter of the word

# then do dfs 4 directions in that current location, base case is if the len(word) == to the ith iteration in the dfs
# we also keep tract of the visited paths in the dfs 
def exist(self, board: list[list[str]], word: str) -> bool:
    directions = [
        (-1, 0),  # Up
        (0, 1),  # Right
        (1, 0),  # Down
        (0, -1),  # Left
    ]

    total_col = len(board[0])
    total_row = len(board)
    first_letter = word[0]

    def addTup(tup1, tup2):
        return tuple(map(lambda i, j: i + j, tup1, tup2))

    def dfs(row, col, i, paths):
        if i == len(word):
            return True

        # if row col is out of bounds
        # if current letter is does not match current board letter
        # if the loc is already  in path
        if (
            row < 0
            or col < 0
            or row >= total_row
            or col >= total_col
            or word[i] != board[row][col]
            or (row, col) in paths
        ):
            return False
        paths.add((row, col))

        for d in directions:
            loc = addTup(d, (row, col))
            if dfs(loc[0], loc[1], i + 1, paths):
                return True

    # find the first letter word index
    for row in range(len(board)):
        for col in range(total_col):
            if board[row][col] == first_letter:
                if dfs(row, col, 0, set()):
                    return True

    return False


res = exist(
    "", [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE"
)

print(res)
