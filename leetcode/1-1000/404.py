from randoms.dsa import *


def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
    total = 0

    def dfs(root, isLeft: bool):
        nonlocal total
        if root is None:
            return
        if isLeft and not root.right and not root.left:
            total += root.val

        if root.left:
            dfs(root.left, True)
        if root.right:
            dfs(root.right, False)

    dfs(root, False)
