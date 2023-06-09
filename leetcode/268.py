def missingNumber(self, nums: list[int]) -> int:
  set_n = set(range(len(nums)+1))
  
  for n in nums:
    if n in set_n:
      set_n.remove(n)
  return list(set_n)[0]
  
print(missingNumber("",[3,0,1]))