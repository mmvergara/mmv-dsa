def search(arr: list, target: int):
    left = 0
    right = len(arr) - 1

    while left <= right:
        print(left,right)
        mid = (left + right) // 2
        if arr[mid] == target:
            return arr[mid]
        if arr[mid] > target:
            right = mid
        else:
            left = mid
    return None


print(search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 9))
