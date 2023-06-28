from dsa import *

def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

    # arr to store all paths
    paths = []

    def dfs(root,s):
        
        # if is a leaf node, append the final string
        if not root.left and not root.right:
            return paths.append(s)
        
        # add string and traverse
        if root.right:
            dfs(root.right,f"{s}->{root.right.val}")
        if root.left:
            dfs(root.left,f"{s}->{root.left.val}")

    dfs(root,str(root.val))

    return paths



