def divisorGame(self, n: int) -> bool:
    aliceTurn = False  # Indicates if it's Alice's turn

    while n != 0 and n != 1:  # Continue the game until n becomes 0 or 1
        i = 0
        less = None

        while less != 0:
            less = n % (n - i)  # Find a divisor by checking remainder
            i += 1

        n = n - (n - i + 1)  # Subtract the divisor from n
        aliceTurn = not aliceTurn  # Switch the turn to the other player

    return aliceTurn  # Return True if Alice wins, False if Bob wins


res = divisorGame("",4)
print(res)


