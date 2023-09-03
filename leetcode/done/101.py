from randoms.dsa import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(1)

# Create the left subtree
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)

# Create the right subtree
root.right = TreeNode(2)
root.right.left = TreeNode(3)
root.right.right = TreeNode(4)

def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    def dfs(left, right):
        # If there are no more subtrees to compare then we traversed the 2 tree's without encountering some mismatch
        if left is None and right is None:
            return 
        
        # if left has value and right has none or vice versa therefore they are not the same
        if left is None or right is None:
            return False
        
        # recursive part where we check the values if they are the same and their subtrees
        return (
            left.val == right.val
            and dfs(left.left, right.right)
            and dfs(left.right, right.left)
        )

    return dfs(root.left, root.right)


print(isSymmetric("", root))
