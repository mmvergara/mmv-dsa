from randoms.dsa import *


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        empty = TreeNode()

        def rec(node1,node2):
            if node1 is None and node2 is None:
                return None
            if node1 is None:
                node1 = empty 
            if node2 is None:
                node2 = empty 

            return TreeNode(node1.val+node2.val,rec(node1.left,node2.left),rec(node1.right,node2.right))

        return rec(root1,root2)
