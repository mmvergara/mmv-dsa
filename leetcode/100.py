# Definition for a binary tree node.
from dsa import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# Perform dfs on both tree's while comparing each values to each other
# if p q is None means that we already are at the leaf and we did not encounter any mismatch
# if p.val != q.val base case is the comparison part where we compare the values of the tree
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs_on_two(p,q):
            print(p,q)
            if p is None and q is None:
                return True

            if p is None or q is None or p.val != q.val:
                return False

            return dfs_on_two(p.left,q.left) and dfs_on_two(p.right,q.right)

        return dfs_on_two(p,q)