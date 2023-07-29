from dsa import *


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
    def rec(ans, n, curNode):
        if n == 0:
            ans.append(curNode)
            return

        curNode = TreeNode(0)
        curNode.left = curNode
        newParent.right = TreeNode(0)
        rec(ans, n - 2, newParent)

        newParent = TreeNode(0)
        newParent.right = TreeNode(0)
        newParent.left = TreeNode(0)
        rec(ans, n - 2, newParent)

    ans = []
    rec(ans, n - 1, TreeNode(0))
    print(ans)
    print(len(ans))


allPossibleFBT("", 7)
