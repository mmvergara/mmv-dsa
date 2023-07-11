from dsa import *


def build(mat):
    g = {}
    for v, u in mat:
        if v not in g:
            g[v] = set()
        if u not in g:
            g[u] = set()
        g[v].add(u)
    return g


def findSmallestSetOfVertices(n: int, edges: List[List[int]]) -> List[int]:
    adj = build(edges)
    nodes = set(adj.keys())
    print(adj)
    visited = set()

    def dfs(n, isStart=False):
        if n in visited:
            return

        if not isStart:
            visited.add(n)

        for neighbors in adj[n]:
            dfs(neighbors)

    for n in nodes:
        dfs(n, True)

    return list(nodes - visited)

    # find all of the reachable nodes from each edge



res = findSmallestSetOfVertices(6, [[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]])
print(res)



    # def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
    #     starts, ends = set(), set()

    #     for x, y in edges:
    #         starts.add(x)
    #         ends.add(y)
        
    #     return starts - ends
