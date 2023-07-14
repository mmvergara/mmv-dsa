def rec(arr, i, subset: list, subsets):
    if i == len(arr):
        subsets.append(subset.copy())
    else:
        rec(arr, i + 1, subset + [arr[i]], subsets)
        rec(arr, i + 1, subset, subsets)


def gen(arr):
    subsets = []
    rec(arr, 0, [], subsets)

    print(subsets)


gen([1, 2, 3])
