
def miniMaxSum(arr):
    total = sum(arr)
    minS = total - max(arr)
    maxS = total - min(arr)
    print(f"{minS} {maxS}")

