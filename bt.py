# generate all possible permutations

x = [1,2,3]
res = []
n = 2
def search(k):
    if k == n:
        print(res)
    else:
        search(k+1)
        res.append(k)
        search(k+1)
        res.pop()







search(0)




























