
def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
    arr = sorted(arr)
    interval = None
    
    for i in range(1,len(arr)):
        if interval is None:
            interval = arr[i] - arr[i-1]

        if abs(arr[i] - arr[i-1]) != interval:
            return False

    return True


