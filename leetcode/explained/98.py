from randoms.dsa import *

# LEARNED: when dealing threshold you can use variables to keep tract of it.

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, left, right):
            if node is None:
                return True

            if not (left < node.val and node.val < right):
                return False

            return dfs(node.left, left, node.val) and dfs(node.right, node.val, right)

        return dfs(root, float("-inf"), float("inf"))
