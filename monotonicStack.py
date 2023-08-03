class monoDecStack:
    def __init__(self) -> None:
        self.stack = []

    def push(self, val):
        if len(self.stack) == 0:
            self.stack.append(val)
            return

        while self.stack and self.stack[-1] < val:
            self.stack.pop()
        self.stack.append(val)

    def isEmpty(self):
        return len(self.stack) == 0

    def pop(self):
        if self.isEmpty():
            raise "Stack is Empty"
        return self.pop()

    def __repr__(self) -> str:
        print(self.stack)
        return ""


s = monoDecStack()
s.push(3)
s.push(4)
print(s)
