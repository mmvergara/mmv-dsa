from randoms.dsa import *

# When it comes to comparisons of tree isSameTree logic is possibly a solution


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None and subRoot is None:
            return True
        if root is None or subRoot is None:
            return False

        def isSameTree(node1, node2):
            if node1 is None and node2 is None:
                return True
            if node1 is None or node2 is None:
                return False

            return (
                node1.val == node2.val
                and isSameTree(node1.left, node2.left)
                and isSameTree(node1.right, node2.right)
            )

        # isSameTree just see's if both trees are the same, but it doesnt count for subtrees
        if isSameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
