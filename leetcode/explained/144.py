from dsa import *
# get
# left
# right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node,ans):
            if node is None:
                return
            ans.append(node.val)
            dfs(node.left,ans)
            dfs(node.right,ans)
        ans = []
        dfs(root,ans)
        return ans