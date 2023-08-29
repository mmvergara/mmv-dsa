from randoms.dsa import *

# left
# right
# visit


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node, ans):
            if node is None:
                return
            dfs(node.left, ans)
            dfs(node.right, ans)
            ans.append(node.val)

        ans = []
        dfs(root, ans)
        return ans
