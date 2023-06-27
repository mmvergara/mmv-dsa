from dsa import  *

def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
    # if there is no root, then it's impossible to find the targetSum
    if root is None:
        return False

    # initialize the base result to False
    hasSum = False

    # we perform dfs until we reach a leaf node then we see if we matched the targetSum for each leaf node
    def dfs(u,s=0):

        nonlocal hasSum
        
        # we will stop traversing if we already found the targetSum
        if hasSum == True:
            return

        # if we are on a leaf node, check if we found the targetSum
        if u.right is None and u.left is None:
            if (s+u.val) == targetSum:
                hasSum = True
            return
        
        # traverse binary tree
        if u.right:
            dfs(u.right,s+u.val)
        if u.left:
            dfs(u.left,s+u.val)

    dfs(root)
    return hasSum


