
def solve(n):
    print(n)
    money = [500, 200, 100, 50, 20, 10]
    used = 0
    m = 0 
    i = 0
    while m < n:
        print(i,m)
        if i > len(money)-1:
            return -1
        newS = m + money[i]
        
        if newS > n:
            i+=1
        else:
            used+=1
            m = newS
    if m > n:
        return -1
    return used


