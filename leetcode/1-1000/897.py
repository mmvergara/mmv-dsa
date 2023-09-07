from randoms.dsa import *

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        ans = None
        cur = None

        def dfs(node):
            nonlocal cur
            nonlocal ans

            if node is None:
                return None

            dfs(node.left)
            if ans is None:
                ans = TreeNode(node.val)
                cur = ans
            else:
                cur.right = TreeNode(node.val)
                cur = cur.right
            
            dfs(node.right)

        dfs(root)
        return ans

