from dsa import *



class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def rec(node,curB):
            nonlocal ans

            if node is None:
                return

            curB += str(node.val)

            if node.left is None and node.right is None:
                ans += int(curB,2)
                return

            rec(node.left,curB)
            rec(node.right,curB)
            
        rec(root,"")
        return ans


