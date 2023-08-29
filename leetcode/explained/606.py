from randoms.dsa import *


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:

        def rec(node):
            if node is None:
                return ""
            lr = rec(node.left)
            rr = rec(node.right)

            if lr == "" and rr == "":
                return f"{node.val}"

            l = f"({lr})" 
            r = f"({rr})" if rr != "" else ""

            return f"{node.val}{l}{r}"

        return rec(root)

