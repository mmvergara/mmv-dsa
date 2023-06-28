
def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    # create a set to store memory locations of nodes
    mset = set()

    # traverse in headNode A
    currentA = headA
    while currentA:
        # add the memory address of each node in the set
        mset.add(id(currentA))
        currentA = currentA.next

    
    # traverse in headNode B
    currentB = headB
    while currentB:
        # check if the current mem location is already in set therefore we found the intersection
        if id(currentB) in mset:
            return currentB
        currentB = currentB.next


