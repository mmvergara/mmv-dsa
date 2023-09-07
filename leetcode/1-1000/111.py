from randoms.dsa import *
import sys

# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

def minDepth(self, root: Optional[TreeNode]) -> int:
    # if there is not root then the depth is 0
    if root is None:
        return 0

    # initialize the minimum depth to be highest possible number this system can hold
    minD = sys.maxsize

    # DFS
    def dfs(node,depth=1):
        # we are using the minD as a reference
        nonlocal minD

        # if we are traversing and the depth is already > than minD then it is useless to go further
        if depth > minD:
            return

        # if it is a leaf node then we calculate the minD
        if not node.right and not node.left:
            minD = min(minD,depth)

        # if it's not a leaf node we keep traversing while incrementing the depth+1
        if node.right:
            dfs(node.right, depth+1)
        if node.left:
            dfs(node.left, depth+1)
        
        
    dfs(root)
    return minD 