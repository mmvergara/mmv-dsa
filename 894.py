from dsa import *


def createSym(k):
    # check if there is a possible symmetric k
    i = 1
    possible = False
    while i < k:
        i = i + (i + 1)
        if i == k:
            possible = True
            continue
    if not possible:
        return None

    # create the symmetric

    # k -= because of the root node, is now a
    k -= 1
    root = TreeNode(0)

    # apply dfs
    # while k is not 0 keep adding 2 nodes on leafs
    while k != 0:

        def dfs(node):
            nonlocal k
            if node.right is None and node.left is None:
                node.right = TreeNode(0)
                node.left = TreeNode(0)
                k -= 2
                return
            dfs(node.left)
            dfs(node.right)

        dfs(root)
    return root


def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
    if n % 2 == 0:
        return []
    k = (n // 2) - 1
    ans = []

    def rec(n, path=[]):
        nonlocal ans
        if n == 0:
            print(path)
            root = TreeNode(0)
            current = root
            for p in path:
                if p == "left":
                    current.left = TreeNode(0)
                    current.right = TreeNode(0)
                    current = current.left
                else:
                    current.right = TreeNode(0)
                    current.left = TreeNode(0)
                    current = current.right
            current.left = TreeNode(0)
            current.right = TreeNode(0)
            ans.append(root)
            return
        rec(n - 1, path + ["left"])
        rec(n - 1, path + ["right"])

    rec(k)

    # create symettric one
    sym = createSym(k)
    if sym:
        ans.append(sym)
    return ans



res = allPossibleFBT("",11)
print(res)
