from randoms.dsa import *
# in order left , visit, right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def dfs(ans, node):
            if node is None:
                return
            dfs(ans, node.left)
            ans.append(node.val)
            dfs(ans, node.right)

        dfs(ans, root)
        print(ans)
        return ans
