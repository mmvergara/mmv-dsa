g = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B", "Z"],
    "E": ["B", "F"],
    "F": ["C", "E"],
    "Z": [],
} 

visited = set()


def dfs(graph, source, target, path: list):
    path.append(source)
    if source == target:    
        return path.copy()

    if source in visited:
        return None
    visited.add(source)

    for n in graph[source]:
        res = dfs(graph, n, target, path.copy())
        if res is not None:
            return res

    return "WOW"


res = dfs(g, "A", "ZG", [])
print(res)
print("done")
