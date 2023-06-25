from dsa import *
def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

    head = ListNode()
    current = head


    # is it just like the merging part of the merge sort
    # loop through both of the list at the same time comparing each values
    while list1 is not None and list2 is not None:
        if list1.val < list2.val:
            current.next = list1
            current = current.next
            list1 = list1.next
        else:
            current.next = list2
            current = current.next
            list2 = list2.next


    # if one of the list are empty we can add the remaining elements in the LL
    while list1 is not None:
        current.next = list1
        current = current.next
        list1 = list1.next

    while list2 is not None:
        current.next = list2
        current = current.next
        list2 = list2.next
    return head.next