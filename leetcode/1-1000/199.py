from randoms.dsa import *


def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    ans = {}

    def dfs(root, depth):
        nonlocal ans
        if root is None:
            return

        ans[depth] = root.val

        dfs(root.left)
        dfs(root.right)

    dfs(root, 0)
    print(ans)
    return
