from dsa import *

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        def rec(node,val):
            if node is None:
                return None

            if node.val == val:
                return node

            if val < node.val:
                return rec(node.left,val)
            else:
                return rec(node.right,val)


        return rec(root,val)

