# QUEUE DS
class MyQueue:

    def __init__(self):
        self.stack = []
        
    def push(self, x: int) -> None:
        self.stack.insert(0,x)

    def pop(self) -> int:
        item = self.stack[-1]
        del self.stack[-1]
        return item
        
    def peek(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return len(self.stack) < 1
        



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()