graph = {
    "a": {"b": 5, "c": 3},
    "b": {"a": 5, "c": 1, "d": 4},
    "c": {"a": 3, "b": 1, "d": 6},
    "d": {"b": 4, "c": 6},
}


# shortest path to a - b is 8


def dijk(graph: dict, start: str, target: str):
    dist = graph.copy()
    for x in dist.keys():
        dist[x] = (float("inf"), None)
    # dist =  key: (distance,lastNode)

    cDist = 0
    lastStart = None

    curNode = start
    while curNode != target:
        shortestNode = None
        shortestNodeDistance = None

        for n in graph[curNode].keys():
            if lastStart == n or n == curNode:
                continue
            newD = cDist + graph[curNode][n]

            if newD < dist[n][0]:
                dist[n] = (newD, curNode)
            if shortestNode is None or shortestNodeDistance > newD:
                shortestNodeDistance = newD
                shortestNode = n
        print(f"shortest node {shortestNode}")
        lastStart = curNode
        curNode = shortestNode
        print(curNode)
        if curNode == target:
            print("Found it")
    print(dist)

    pass


dijk(graph, "a", "d")
