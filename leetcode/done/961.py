
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        st = set()
        for n in nums:
            if n in st:
                return n
            st.add(n)
            

