#The number of nodes in the tree is in the range [1, 104].
#The values of the nodes of the tree are unique.
#target node is a node from the original tree and is not null.

def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
    # just search the cloned tree node and compare if similar val to the target
    # because every value in a tree node is unique
    def dfs(cloned):
        if cloned is None:
            return None

        stack = []
        
        stack.append(root)

        while stack:
            node = stack.pop()

            if node.val == target.val:
                return node 
            
            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)

        return None
    dfs(original,cloned)






