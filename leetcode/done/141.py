from randoms.dsa import *


# We modify each node that we are traversing ( Modify in anyway ex. add a value or in my case changed the value to "done")

def hasCycle(self, head: Optional[ListNode]) -> bool:
    current = head
    while current:
        if current.val == "done":
            return True
        current.val = "repeat"
        current = current.next
    return False
