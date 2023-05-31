def can_reach_destination(arr):
    rows = len(arr)
    cols = len(arr[0])

    # Create a visited array to keep track of visited cells
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    
    # Define the directions: up, down, left, and right
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1,1), (-1,1), (-1,-1), (1,-1)]

    def dfs(row, col):
        # Mark the current cell as visited
        visited[row][col] = True
        print(visited)
        # Check if the current cell is the destination
        if arr[row][col] == "D":
            return True

        # Explore the adjacent cells in all directions
        for dx, dy in directions:
            new_row = row + dx
            new_col = col + dy

            # Check if the new cell is within the array boundaries
            if 0 <= new_row < rows and 0 <= new_col < cols:
                # Check if the new cell is not a wall and has not been visited before
                if arr[new_row][new_col] != "X" and not visited[new_row][new_col]:
                    # Recursively explore the new cell
                    if dfs(new_row, new_col):
                        return True

        return False

    # Find the starting position of "S"
    for i in range(rows):
        for j in range(cols):
            if arr[i][j] == "S":
                return dfs(i, j)

    return False

# Example usage:
x = [
    ["O","X","D"],
    ["X","O","O"],
    ["S","X","O"]
]
print(can_reach_destination(x))
