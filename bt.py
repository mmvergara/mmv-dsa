# generate all possible permutations

x = [1, 2, 3]
ss = []
n = 2

total = []


def search(k):
    if k == n:
        total.append(ss.copy())
    else:
        search(k + 1)
        ss.append(k+1)
        search(k + 1)
        ss.pop()

search(0)
print(total)
