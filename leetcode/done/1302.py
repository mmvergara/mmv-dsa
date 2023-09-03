from randoms.dsa import *

def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
    # keep tract of the max depth
    md = 0
    # freq of depth: sum of nodes in that depth
    f = {}

    def dfs(root,dp=0):
        nonlocal md
        if dp in f:
            f[dp]+=root.val
        else:
            f[dp] = root.val
        md = max(md,dp)

        if root.left:
            dfs(root.left,dp+1)
        if root.right:
            dfs(root.right,dp+1)

    dfs(root)
    return f[md]
