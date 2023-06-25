from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
def maxDepth(self, root: Optional[TreeNode]) -> int:
    if not root: return 0
    highest_depth = 0
    def search(root,depth=1):

        # every time we travel to a subtree we will take the maximum depth
        nonlocal highest_depth
        if not root:
            highest_depth = max(depth,highest_depth)
            return

        if not root.left and not root.right:
            highest_depth = max(depth,highest_depth)
            return 

        # upon travelling more downwards on subtree we increment the new depth
        if root.left:
            search(root.left,depth+1)
        if root.right:
            search(root.right,depth+1)
    search(root)
    return highest_depth
