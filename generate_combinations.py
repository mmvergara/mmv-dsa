def generate_combinations(items):

    for i in range(len(items)):
        for j in range(i,len(items)-i):
            print(j)

generate_combinations([1,2,3,4,5])
