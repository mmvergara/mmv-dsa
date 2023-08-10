from dsa import *


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def getHeight(node):
            if node is None:
                return 0

            left_height = getHeight(node.left)
            right_height = getHeight(node.right)

            # If any subtree is not balanced, return -1
            if (
                left_height == -1
                or right_height == -1
                or abs(left_height - right_height) > 1
            ):
                return -1

            return max(left_height, right_height) + 1

        return getHeight(root) != -1
