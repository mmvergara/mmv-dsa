from dsa import *

def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
    
    def rec(l,r):
        nonlocal nums
        if l >= r:
            return None
        m = (l + r) // 2

        leftNode = rec(l,m)
        rightNode = rec(m+1,r)
        return TreeNode(nums[m],leftNode,rightNode)
    return rec(0,len(nums))
    
        

print(sortedArrayToBST("",[-10,-3,0,5,9]))