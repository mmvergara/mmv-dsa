# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
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