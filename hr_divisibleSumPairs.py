
def divisibleSumPairs(n, k, arr):
    cs = {}
    pairs = 0
    for i in range(n):
        i = n - i - 1
        mod = arr[i]%k
        if mod in cs:
            cs[mod].append(i)
        else:
            cs[mod] = [i]

        modComplement = (k - (arr[i])) % k
        if modComplement in cs:
            for j in cs[modComplement]:
                if i < j:
                    print(f"({i},{j})")
                    pairs+=1
    return pairs

res = divisibleSumPairs(6,3,[1,3,2,6,1,2])
print(res)
