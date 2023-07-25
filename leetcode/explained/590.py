from dsa import *


class Solution:
    def postorder(self, root) -> List[int]:
        if root is None:
            return []
        ans = []

        def dfs(ans, node):
            if node is None:
                return

            for n in node.children:
                dfs(ans, n)
                ans.append(n.val)

        dfs(ans, root)
        ans.append(root.val)
        print(ans)
        return ans
