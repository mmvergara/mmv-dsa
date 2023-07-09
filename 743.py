import heapq
import collections
from dsa import *
def networkDelayTime(times: List[List[int]], n: int, k: int) -> int:
    edges = collections.defaultdict(list)
    print(edges)

    for u,v,w in times:
        edges[u].append((v,w))

    minHeap = [(0,k)]
    visit = set()
    maxCost = 0

    while minHeap:
        #pop from heap
        weight1, node1 = heapq.heappop(minHeap)

        #keep tract of visited nodes
        if node1 in visit:
            continue
        visit.add(node1)
        
        # reseat the max cost
        maxCost = max(maxCost,weight1)
        
        # go through all of the neighboring nodes
        for node2,weight2 in edges[node1]:
            if node2 not in visit:
                # add the last weight from the current node to the neighboring node to be visited
                heapq.heappush(minHeap,(weight2+weight1,node2))
    return maxCost if len(visit) == n else -1

res = networkDelayTime([[2,1,1],[2,3,1],[3,4,1]],4,2)
print(res)