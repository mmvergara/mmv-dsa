from collections import deque
from randoms.dsa import *


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        q = deque([(root, 0)])
        ans = []
        while q:
            (node, level) = q.pop()
            if len(ans) < (level + 1):
                ans.append([node.val])
            else:
                if level % 2 == 0:
                    ans[level].append(node.val)
                else:
                    ans[level].insert(0, node.val)

            if node.left:
                q.appendleft((node.left, level + 1))
            if node.right:
                q.appendleft((node.right, level + 1))
        return ans
