from dsa import *

# learned, for getting array num indices in correlations to the other array, we can just use a hash table to the array 2 result

# ex arr1 [1,2,3]
# arr 2 [3,1,2]
# proccess the arr so that for each value will be a key in the hashmap to get the next greater
# {
#   1: res
#   2: res
#   3: res
# }
# then just loop on arr 1 using map[arr[i]]


def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    stack = []
    next_greater = {}

    # Preprocess nums2 to find the next greater element for each element
    for num in nums2:
        while stack and stack[-1] < num:
            next_greater[stack.pop()] = num
        stack.append(num)
    print(next_greater)

    # Initialize the result list with -1
    res = [-1] * len(nums1)

    # Fill the result list with the next greater element for each element in nums1
    for i, num in enumerate(nums1):
        if num in next_greater:
            res[i] = next_greater[num]

    return res


nextGreaterElement("", nums1=[1, 3, 5, 2, 4], nums2=[6, 5, 4, 3, 2, 1, 7])
