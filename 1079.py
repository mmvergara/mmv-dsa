def numTilePossibilities(self, tiles: str) -> int:
        
    def backtrack(sequence, remaining):
        if not remaining:
            sequences.append(sequence)
            return
        
        for i in range(len(remaining)):
            new_sequence = sequence + remaining[i]
            new_remaining = remaining[:i] + remaining[i+1:]
            backtrack(new_sequence, new_remaining)

    sequences = []

    backtrack("",tiles)
    return sequences



print(numTilePossibilities("","AAB"))
