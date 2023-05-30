class Queue:
    def __init__(self,initialVal) -> None:
        self.head = {"v":initialVal,"nextLine":None}
        self.tail = self.head
        pass

    def addVal(self,v):
        self.tail['nextLine'] = {"v":v,"nextLine":None}
    
    def printQueue(self):
        print(self.head)



q = Queue(1)

q.printQueue()


def getLengthByHead(head):
    if (head["nextLine"] == None):
        return 1
    return 1 + getLengthByHead(head["nextLine"])

print(getLengthByHead(q.head))

    