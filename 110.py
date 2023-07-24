from dsa import *

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def getHeight(root):
            if root is None:
                return 0
            
            lh = 1 + getHeight(root.left)
            rh = 1 + getHeight(root.right)

            return max(lh,rh)
        

        return abs(getHeight(root.right) - getHeight(root.left)) <= 1
        


        