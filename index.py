import heapq


heap = []
heapq.heappush(heap,4)
heapq.heappush(heap,8)
heapq.heappush(heap,1)
heapq.heappush(heap,-7)
heapq.heappush(heap,24)
heapq._heapify_max(heap)
print(heap)
