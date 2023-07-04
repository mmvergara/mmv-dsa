from dsa import *
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # same as merge sort merging
    def mergeLL(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        tempHead = ListNode(0)
        current = tempHead

        while l1 and l2:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next  
            current = current.next
        
        if l1:
            current.next = l1
        elif l2:
            current.next = l2
        return tempHead.next


    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # base case
        if not lists:
            return None
        
        # pre add the first ll 
        temp = [lists[0]]

        # compare the current end ll of temp to the new ll to be merged and merge them
        for i in range(len(lists)-1):
            merged = self.mergeLL(temp[i],lists[i+1])
            temp.append(merged)
        return temp[-1]









