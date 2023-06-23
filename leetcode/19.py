from dsa import *


def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    before_left = None

    # initialize left and right pointer
    left = head
    right = head
    
    # right pointer goes to nth element
    for _ in range(n):
        right = right.next
        
    # use the right pointer so when the right pointer is at the end, the left pointer is pointer directly to the Nth element from end to be removed
    while right:
        before_left = left
        left = left.next
        right = right.next

    # now the right pointer is at the end
    # and the left pointer is at the element to be removed


    # if there is no before left means that the right pointer already is at the end therefore the first element in the array in the one being removed we just return the next element in the LL
    if before_left is None:
        return left.next
    
    # now we have the before_left we just need to connect it to the left.next because left is pointed directly to the node that is being removed.
    before_left.next = left.next
    return head
    

