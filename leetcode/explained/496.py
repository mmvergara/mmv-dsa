
# Uses Monotonic stack 
def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
    # initialize stack and dictionary
    stack = []
    dic = {}
    
    # loop through nums 2 which contains all of the reference array
    for i in range(len(nums2)):

        curT = (nums2[i],i)

        # if current num is less than the top of the stack
        # keep popping the stack and process popped values tobe the dic[value] = currentT
        while stack and nums2[i] > stack[-1][0]:
            sv,si = stack.pop()
            dic[sv] = curT
        # finally push the current to the top of she stack
        stack.append(curT)
    
    for i in range(len(nums1)):
        if nums1[i] in dic:
            nums1[i] = dic[nums1[i]][0]
        # if there is no greater next element put -1 as a value
        else:
            nums1[i] = -1

    return nums1


nextGreaterElement("",[4,1,2],[1,3,4,2])
