from randoms.dsa import *

def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
    # remove duplicates
    nums1 = list(set(nums1))
    nums2 = list(set(nums2))
    nums3 = list(set(nums3))
    
    # get the max size between 3 arrs
    n = max(len(nums1),len(nums2),len(nums3))
    
    #initialize set and result arr 
    hset = set()
    res = []

    # addToSet helper function to handle adding logic in the set
    def addToSet(n):
        if n in hset:
            res.append(n)
            hset.remove(n)
            return
        hset.add(n)

    # loop through all of the elements in the array
    i = 0
    while i < n:
        if i < len(nums1):
            addToSet(nums1[i])
        if i < len(nums2):
            addToSet(nums2[i])
        if i < len(nums3):
            addToSet(nums3[i])
        i+=1
    
    return res

res = twoOutOfThree("",[1,1,3,2],[2,3],[3])
print(res)










# python syntax sugar one liner
# make each one a set to remove duplicates and use set operators
# we first get the intersection of all of the set combinations
# then get the union of the 3 result


#def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
	#return set(nums1) & set(nums2) | set(nums2) & set(nums3) | set(nums1) & set(nums3)


