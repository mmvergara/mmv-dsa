# https://www.hackerrank.com/challenges/the-birthday-bar/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
from collections import deque

def birthday(arr, d, m):

    curArr = deque([arr[i] for i in range(m)])
    right = m
    res = 0

    if sum(curArr) == d:
        res+=1

    while right < len(arr):
        curArr.popleft()
        curArr.append(arr[right])
        if sum(curArr) == d:
            res+=1
        right+=1

    return res


print(birthday([4],4,1))


    
