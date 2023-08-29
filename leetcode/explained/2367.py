from randoms.dsa import *


def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
    n = len(nums)
    ans = 0
    st = set()
    for i in range(n):
        st.add(nums[i])
        if (nums[i]-diff) in st and (nums[i]-diff-diff) in st:
            ans+=1
    return ans


print(arithmeticTriplets("", nums=[0, 1, 4, 6, 7, 10], diff=3))
