# def rotateLeft(d, arr):
#     d = d % len(arr)
#     return [*arr[d:], *arr[:d]]
#     pass


def rotateLeft(d, arr):
    # Adjust d to ensure it's within the range of array size
    d = d % len(arr)

    # Reverse the first d elements
    reverse(arr, 0, d - 1)
    print(arr)

    # Reverse the remaining elements
    reverse(arr, d, len(arr) - 1)
    print(arr)

    # Reverse the entire array to restore the original order
    reverse(arr, 0, len(arr) - 1)
    print(arr)

    # Return the modified array with left rotation applied
    return arr


def reverse(arr, start, end):
    # Swap elements at start and end indices iteratively
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


res = rotateLeft(3, [1, 2, 3, 4, 5])
