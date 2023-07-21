def gen(arr: list):
    combinations = []

    def rec(combinations, combination, i):
        if i == len(arr):
            combinations.append(combination[:])
            return
        rec(combinations, combination + [arr[i]], i + 1)
        rec(combinations, combination, i + 1)

    rec(combinations, [], 0)

    print(combinations)


gen(["A", "B", "C"])
