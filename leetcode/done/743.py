from randoms.dsa import *
import heapq


def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
    # source : [ ( weight , target )]
    def build(times):
        ans = {}
        for n in times:
            if n[0] in ans:
                ans[n[0]].append((n[2], n[1]))
            else:
                ans[n[0]] = [(n[2], n[1])]
        return ans

    visited = set()
    graph = build(times)

    queue = [(0, k)]
    dist = {}
    while queue:
        curW, curN = heapq.heappop(queue)
        if curN in visited:
            continue
        visited.add(curN)
        if curN not in graph:
            continue
        for tW, tN in graph[curN]:
            if tN == k:
                continue
            totalDistFromCurn = tW + curW
            if tN not in dist:
                dist[tN] = totalDistFromCurn
                heapq.heappush(queue, (totalDistFromCurn, tN))
                continue
            if dist[tN] > totalDistFromCurn:
                dist[tN] = totalDistFromCurn
                heapq.heappush(queue, (totalDistFromCurn, tN))

    if len(visited) != n:
        return -1
    if len(dist) == 0:
        return 0
    print(dist)
    return max(dist.values())


res = networkDelayTime(
    "",
    [
        [4, 3, 76],
        [1, 4, 70],
        [1, 3, 37],
        [1, 2, 53],
        [3, 2, 66],
        [3, 4, 22],
        [5, 4, 52],
        [2, 1, 23],
        [5, 1, 27],
        [4, 5, 88],
        [5, 2, 26],
        [2, 4, 41],
        [4, 2, 66],
        [4, 1, 93],
        [3, 5, 78],
        [2, 5, 9],
        [5, 3, 50],
        [3, 1, 17],
        [1, 5, 12],
        [2, 3, 87],
    ],
    5,
    5,
)
print(res)
