from collections import Counter

def topKFrequent(self, nums: list[int], k: int) -> list[int]:
    return [k for k,_ in Counter(nums).most_common(k)]

    # occurences_count = {} 
    # for n in nums:
    #     if n in occurences_count:
    #         occurences_count[n]+=1
    #     else:
    #         occurences_count[n] = 1

    # out_arr = []
    # for i in range(k):
    #     max_value = max(occurences_count.values())
    #     max_key = [key for key, value in occurences_count.items() if value == max_value]
    #     del occurences_count[max_key[0]]
    #     out_arr.append(max_key[0])
    # return out_arr

res = topKFrequent("",[1,1,1,2,2,3],2)
print(res)