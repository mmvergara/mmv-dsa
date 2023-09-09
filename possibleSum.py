def solve(amount, nums, idx=0):
    nums.sort(reverse=True)

    def rec(s=0, idx=0):
        if s == amount:
            return True

        if s > amount:
            return False

        for i in range(idx, len(nums)):
            if rec(s + nums[i], idx + 1):
                return True
        return False

    return rec()


print(solve(5, []))
