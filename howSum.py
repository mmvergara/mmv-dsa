def howSum(targetSum,nums,memo={}):
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0: return []
    if targetSum < 0 : return None

    for n in nums:
        remainder = targetSum - n
        remainderResult = howSum(remainder,nums,memo)
        if remainderResult is not None:
            memo[targetSum] = [n,*remainderResult]
            return memo[targetSum]

    memo[targetSum] = None       
    return None
    




res = howSum(300,[7,15])
print(res)
