def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    if not root:
        return False
    if not root.right or not root.left:
        return False

    symmetric = True

    def dfs_tree(root):
        nonlocal symmetric
        if root is None:
            return False

        stack = [root]

        left = []
    
        while stack:
            current = stack.pop()
            print(current.val)

            if current.left:
                left.append(current.left.val)
                stack.append(current.left)

            if current.right:
                if left[-1] != current.right.val:
                    symmetric = False
                    break
                stack.append(current.right)
        
    dfs_tree(myTree)

    return symmetric
