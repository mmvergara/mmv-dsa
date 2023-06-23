# Done
def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
    stack = []
    dic = {}
    for i in range(len(nums2)):
        curT = (nums2[i],i)
        while stack and nums2[i] > stack[-1][0]:
            sv,si = stack.pop()
            dic[sv] = curT
        stack.append(curT)
    
    for i in range(len(nums1)):
        if nums1[i] in dic:
            nums1[i] = dic[nums1[i]][0]
        else:
            nums1[i] = -1
    print(nums1)

    return nums1


nextGreaterElement("",[4,1,2],[1,3,4,2])
