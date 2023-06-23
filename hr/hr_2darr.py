#Done
def hourglassSum(arr):
    # Find the centers
    print(arr)
    centers = []
    for row in range(1,len(arr)-1):
        for col in range(1,len(arr[0])-1):
            centers.append((row,col))
    print(centers)
    maxhg = float("-inf")
    for r,c in centers:
        total = arr[r][c] + arr[r+1][c-1] + arr[r+1][c] + arr[r+1][c+1] + arr[r-1][c-1] + arr[r-1][c] + arr[r-1][c+1]
        maxhg = max(maxhg,total)
