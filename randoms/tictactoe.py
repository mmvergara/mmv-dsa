import os


class TicTacToe:
    def __init__(self) -> None:
        self.initializeGame()
        self.play()

    def play(self):
        self.printGameState()
        boxSelected = None
        while True:
            try:
                boxSelected = int(input("Select Box from 1-9\n")) - 1
                if boxSelected > 8:
                    print("Out of range!")
                    continue
                if boxSelected in self.OBoxes or boxSelected in self.XBoxes:
                    print("Box already selected")
                    continue
                break
            except:
                continue
        if self.currentPlayer == "O":
            self.gameState[boxSelected] = "O"
            self.currentPlayer = "X"
            self.OBoxes.append(boxSelected)
        else:
            self.gameState[boxSelected] = "X"
            self.currentPlayer = "O"
            self.XBoxes.append(boxSelected)
        state = self.checkState()
        if state == "Continue":
            self.play()
        else:
            print(state)

    def printGameState(self):
        os.system("cls")
        print(f"Current Player {self.currentPlayer}")
        print("================")
        print("    ", self.gameState[0], self.gameState[1], self.gameState[2])
        print("    ", self.gameState[3], self.gameState[4], self.gameState[5])
        print("    ", self.gameState[6], self.gameState[7], self.gameState[8])
        print("================")

    def checkState(self) -> str:
        if self.check_if_won(self.OBoxes):
            return "O Won"
        if self.check_if_won(self.XBoxes):
            return "X Won"
        if len(self.OBoxes) + len(self.XBoxes) == 9:
            return "Draw"
        return "Continue"

    def initializeGame(self):
        self.currentPlayer = "O"
        self.OBoxes = []
        self.XBoxes = []
        self.gameState = [
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
        ]

    def check_if_won(self, pBoxes):
        winning_states = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 4, 5],
            [2, 4, 6],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
        ]
        return any(
            True if all([True if wsb in pBoxes else False for wsb in ws]) else False
            for ws in winning_states
        )


game = TicTacToe()

