def containsDuplicate(self, nums):
    seen = {}
    for x in nums:
        if x in seen:
            return True
        else:
            seen[x] = x
    return False

print(containsDuplicate(2,[1,2]))