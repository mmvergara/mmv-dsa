from randoms.dsa import *


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def inRange(v, l, h):
            return v >= l and v <= h

        def rec(node):
            if node is None:
                return 0
            ans = 0
            if inRange(node.val, low, high):
                ans = node.val

            ans += rec(node.left)
            ans += rec(node.right)
            return ans

        return rec(root)
