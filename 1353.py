from randoms.dsa import *
import heapq


def maxEvents(self, events: List[List[int]]) -> int:
    events = sorted(events, key=lambda x: [x[1], x[0]])
    x = 0

    print(events)
    # process data 0(N)
    xEvents = set()
    n = len(events)
    heap = []
    for i in range(n):
        heapq.heappush(heap, ((events[i][1] - events[i][0]), i))

    attended = 0
    deadRanges = set()
    while heap:
        dur, idx = heapq.heappop(heap)
        if idx in xEvents:
            continue

        nI = idx + 1
        pI = idx - 1

        if events[idx][0] != events[idx][1]:
            deadRanges(events[idx][0])
        else:
            if events[idx][0] in deadRanges:
                continue

        attended += 1

        # blacklist the next/previous event if it cannot be attended
        # if the event is in range and not already blacklisted
        if nI not in xEvents and nI < n:
            if events[idx][1] < events[nI][0]:
                xEvents.add(nI)

        if pI not in xEvents and pI >= 0:
            if events[idx][1] < events[pI][0]:
                xEvents.add(pI)

    return attended


print(maxEvents("", [[1, 4], [4, 4], [2, 2], [3, 4], [1, 1]]))
