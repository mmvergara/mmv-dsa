from randoms.dsa import *

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node,oArr):
            if node is None:
                return

            if node.left is None and node.right is None:
                oArr.append(node.val)
                return
            
            dfs(node.left,oArr)
            dfs(node.right,oArr)
        
        r1 = []
        r2 = []
        dfs(root1,r1)
        dfs(root2,r2)
        return r1 == r2
