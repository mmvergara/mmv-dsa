from dsa import *


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
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        return (
            left.val == right.val
            and dfs(left.left, right.right)
            and dfs(left.right, right.left)
        )

    return dfs(root.left, root.right)


print(isSymmetric("", root))
