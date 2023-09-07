# USE DFS TO COUNT THE MAX DEPTH, 
def maxDepth(self, root, depth=0) -> int:
    if not root:
        return 0
    
    # keep tract of max depth as we traverse
    maxd = 0

    def dfs(root, depth=0):
        nonlocal maxd
        maxd = max(maxd, depth + 1)
        if not root or not root.children:
            return

        for c in root.children:
            # incremenet depth as we move forward
            dfs(c, depth + 1)

    dfs(root)
    return maxd
