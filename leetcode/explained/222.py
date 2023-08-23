class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        def dfs(root,count):
            if root is None:
                return count
            return 1 + dfs(root.left,count) + dfs(root.right,count)
        
        return dfs(root,0)
