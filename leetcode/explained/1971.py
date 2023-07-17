from dsa import *


def build(edges):
    graph = {}
    for u, v in edges:
        if u not in graph:
            graph[u] = set()
        if v not in graph:
            graph[v] = set()
        graph[u].add(v)
        graph[v].add(u)
    return graph


def validPath(n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    graph = build(edges)
    print(graph)
    visited = set()

    def dfs(graph, s, d):
        if s == d:
            return True

        if s in visited:
            return
        visited.add(s)

        for v in graph[s]:
            if dfs(graph, v, d):
                return True
        return False

    return dfs(graph, source, destination)
