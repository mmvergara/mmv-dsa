class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mp1 = {}
        mp2 = {}

        for i in range(len(nums1)):
            if nums1[i] in mp1:
                mp1[nums1[i]]+=1
            else:
                mp1[nums1[i]]= 1

        for i in range(len(nums2)):
            if nums2[i] in mp2:
                mp2[nums2[i]]+=1
            else:
                mp2[nums2[i]]= 1
        intersection = []
        for k in mp1:
            if k in mp2:
                cnt = min(mp1[k],mp2[k])
                for i in range(cnt):
                    intersection.append(k)
        
        return intersection