class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        st = set()
        for x in nums:
            if x == 0:
                continue
            if x not in st:
                st.add(x)

        return len(st)
