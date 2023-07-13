graph = [
    [0, 1],
    [1, 2],
    [3, 4],
    [4, 5],
    [6, 8],
    [11,10],
    [10,20]
]


def build(mat):
    g = {}
    for v, u in mat:
        if v not in g:
            g[v] = set()
        if u not in g:
            g[u] = set()
        g[v].add(u)
        g[u].add(v)
    return g


def solve(graph: dict):
    nodes = list(graph.keys())

    visitedNodes = set()
    res = 0

    def dfs(v):
        if v in visitedNodes:
            return
        visitedNodes.add(v)
        for n in graph[v]:
            dfs(n)

    for n in nodes:
        if n in visitedNodes:
            continue
        dfs(n)
        res += 1

    print(res)
    print(nodes)


solve(build(graph))
