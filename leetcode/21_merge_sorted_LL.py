# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        head = ListNode()
        current = head
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                current.next = list1
                current = current.next
                list1 = list1.next
            else:
                current.next = list2
                current = current.next
                list2 = list2.next

        while list1 is not None:
            current.next = list1
            current = current.next
            list1 = list1.next

        while list2 is not None:
            current.next = list2
            current = current.next
            list2 = list2.next
        return head.next