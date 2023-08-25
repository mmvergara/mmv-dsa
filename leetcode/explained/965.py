from dsa import *


class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, val):
            if node is None:
                return True

            if node.val != val:
                return False

            return dfs(node.right, val) and dfs(node.left, val)

        return dfs(root, root.val)
