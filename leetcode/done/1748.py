
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        abnd = set()
        uniq = set()


        for n in nums:
            if n in abnd:
                continue
            if n in uniq:
                abnd.add(n)
                uniq.remove(n)
            else:
                uniq.add(n)

        return sum(uniq)

