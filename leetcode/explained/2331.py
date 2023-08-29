from randoms.dsa import *

class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def rec(node):
            if node.val == 0:
                return False
            if node.val == 1:
                return True
            
            l = rec(node.left)
            r = rec(node.right)
            if node.val == 2:
                return l or r
            elif node.val == 3:
                return l and r
        return rec(root)

            
