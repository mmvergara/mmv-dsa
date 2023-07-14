# largest Graph Component

ajl = {
        0:[8,1,5],
        1:[0],
        5:[0,8],
        8:[0,5],
        2:[3,4],
        3:[2,4],
        4:[3,2],

        200:[100],
        100:[200]
        }


def solve(graph):
    nodes = list(graph.keys())
    
    visited = set()
    # dfs keeping tract of the nodes we are traversing
    def dfs(n,traversedNodes):
        if n in visited:
            return
        visited.add(n)
        traversedNodes.append(n)
        for neighbors in graph[n]:
            dfs(neighbors,traversedNodes)
        return traversedNodes
    
    # traverse the nodes
    allComponents = []
    for n in nodes:
        res = dfs(n,[])
        if res is not None:
            allComponents.append(res)

    print(allComponents)
    print(nodes)



solve(ajl)
