class Node:
    def __init__(self,val,nextVal=None) -> None:
        self.val = val
        self.nextVal = nextVal
class MyLinkedList:
    def __init__(self,initialVal) -> None:
        firstNode = Node(initialVal)
        self.head = firstNode
        self.tail = firstNode
        self.length = 1
        pass

    def addNodeHead(self,nodeVal):
        newNode = Node(nodeVal)
        previosHead = self.head
        self.head = newNode
        self.head.nextVal = previosHead
        self.length+=1

    def addNodeTail(self,nodeVal):
        newNode = Node(nodeVal)
        self.tail.nextVal = newNode
        self.tail = newNode
        self.length+=1

    def removeNode(self,nodeValToRemove):
        if nodeValToRemove == self.head.val:
            self.head = self.head.nextVal
            self.length-=1
            return
        
        currentNode = self.head
        lastNode = None
        foundNode = None
        while foundNode is None:
            if currentNode.val == nodeValToRemove:
                foundNode = currentNode
            else:
                lastNode = currentNode
                currentNode = currentNode.nextVal
        lastNode.nextVal = foundNode.nextVal
        self.length-=1


    
    def printAll(self):
        outArr = []
        currentNode = self.head
        while currentNode is not None:
            outArr.append(str(currentNode.val))
            currentNode = currentNode.nextVal
        print("["+"] --> [".join(outArr)+"]")




ll = MyLinkedList(1)
ll.addNodeTail(2)
ll.addNodeTail(3)
ll.addNodeTail(3)
ll.addNodeTail(3)
ll.addNodeTail(3)
ll.addNodeTail(4)
ll.addNodeHead(9)

ll.printAll()
    