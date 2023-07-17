from dsa import *


def findJudge(n: int, trust: List[List[int]]) -> int:
    if n == 1:
        return 1

    hasTrustOnSomeone = set()
    allPeople = set()
    trustPoints = {}
    for u, v in trust:
        allPeople.add(u)
        allPeople.add(v)

        hasTrustOnSomeone.add(u)

        if v in trustPoints:
            trustPoints[v] += 1
        else:
            trustPoints[v] = 1

    townJudge = allPeople - hasTrustOnSomeone

    if len(townJudge) == 0:
        return -1
    else:
        res = [x for x in townJudge][0]
        if trustPoints[res] != n - 1:
            return -1
        return [x for x in townJudge][0]
