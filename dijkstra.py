import heapq

graph = {
    "a": {"b": 8, "c": 0},
    "b": {"a": 1, "c": 1, "d": 4},
    "c": {"a": 3, "b": 1, "d": 6},
    "d": {"b": 4, "c": 6},
}


# shortest path to a - b is 8


def dijk(graph: dict, start: str, target: str):
    dist = graph.copy()
    for x in dist.keys():
        dist[x] = (float("inf"), None)
    dist[start] = (0, None)

    visited = set()
    heap = [(0, start)]
    while heap:
        curD, node = heapq.heappop(heap)

        if node in visited:
            continue
        visited.add(node)
        for neighbor, weight in graph[node].items():
            # cur node distance +  neighbor distance
            totalD = weight + curD
            heapq.heappush(heap, (totalD, neighbor))
            if totalD < dist[neighbor][0]:
                # append new min distance
                # append last path
                dist[neighbor] = (totalD, node)
    # backtract reconstruct the path

    curN = target
    path = []
    while curN:
        path.append(curN)
        _, n = dist[curN]
        curN = n
    print(list(reversed(path)))


dijk(graph, "a", "d")
