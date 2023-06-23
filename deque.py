class Node:
    def __init__(self,val=None,next=None,prev=None):
        self.val = val
        self.next = next
        self.prev = prev

    def __repr__(self):
        return f"{{ val:{self.val} , next:{self.next} }}"


class MyDeque:
    def __init__(self,initVal=None):
        self.head = Node(initVal)
        self.tail = self.head


    def push_front(self,val):
        lastHead = self.head
        newNode = Node(val)
        self.head = newNode
        lastHead.prev = self.head
        self.head.next = lastHead 
    
    def pop_front(self):
        val = self.head.val
        self.head = self.head.next
        return val

    def push_back(self,val):
        newNode = Node(val)
        lastTail = self.tail
        self.tail.next = newNode
        newNode.prev = lastTail

    def pop_back(self):
        lastTail = self.tail
        self.tail = self.tail.prev
        return lastTail.val
        


    def __repr__(self):
        strr = "{"
        currentNode = self.head
        while currentNode:
            strr+=f" {currentNode.val}"
            currentNode = currentNode.next
        strr+=" }"
        return strr


a = MyDeque(0)
a.push_back(1)
a.push_back(2)
a.push_back(3)
print(a)
print(a.tail)
        


