from collections import deque
from dsa import *


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        q = deque([(root, 0)])
        print(q)
        ans = []
        while q:
            (node, level) = q.pop()
            if len(ans) < (level + 1):
                ans.append([node.val])
            else:
                ans[level].append(node.val)

            if node.left:
                q.appendleft((node.left, level + 1))
            if node.right:
                q.appendleft((node.right, level + 1))
        print(ans)
        return ans
