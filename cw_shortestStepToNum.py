
def shortest_steps_to_num(num):
    # Initialize a list to store the minimum steps to reach each number from 1 to 'num'.
    # Initialize all values to infinity, except dp[1] which is 0 (no steps needed to reach 1).
    dp = [float('inf')] * (num + 1)
    dp[1] = 0


    # Perform a bottom-up dynamic programming approach to fill the dp list.
    for n in range(1, num):
        print(dp)
        # Update the number n+1 (increment) if it's a more optimal path.
        dp[n + 1] = min(dp[n + 1], dp[n] + 1)

        # Update the number 2*n (double) if it's a more optimal path.
        if 2 * n <= num:
            dp[2 * n] = min(dp[2 * n], dp[n] + 1)

    # The result is stored in dp[num], representing the minimum steps to reach 'num'.
    print(dp,num)
    result = dp[num]

    print(result)
    return result

# Test the function
shortest_steps_to_num(10)
