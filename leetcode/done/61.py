from randoms.dsa import *

node1 = ListNode(1)
node2 = ListNode(2)
node1.next = node2
node3 = ListNode(3)
node2.next = node3
node4 = ListNode(4, ListNode(5))
node3.next = node4


def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    # base case
    if head is None:
        return head

    # Minimizes the number if rotation
    currentNode = head
    size = 0
    while currentNode:
        size += 1
        currentNode = currentNode.next
    k = k % size
    if (k - 1) < 0:
        return head

    # go to kth element using 2 pointers
    slow = head
    fast = head

    # fast pointer advance by kth time
    for _ in range(k - 1):
        fast = fast.next
        if fast == None:
            fast = head

    # traverse until fast pointer is in the end
    while fast.next:
        slow = slow.next
        fast = fast.next

    # notice: now the slow will be the new HEAD

    # go to the tail of the slow
    currentNode = slow
    while currentNode.next:
        currentNode = currentNode.next

    # connect the tail of the slow to the original head
    currentNode.next = head

    # traverse until we intersect the new head which is the slow
    while currentNode.next:
        if id(currentNode.next) == id(slow):
            # break the connection to the new head
            currentNode.next = None
            break
        currentNode = currentNode.next

    # return new head
    return slow


res = rotateRight("", node1, 2)
print(res)
