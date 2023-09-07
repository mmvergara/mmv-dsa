from collections import deque


class MyStack:
    def __init__(self):
        self.queue = deque()
        pass

    def push(self, x: int) -> None:
        self.queue.appendleft(x)
        pass

    def pop(self) -> int:
        if len(self.queue) == 0:
            raise "EMPTY"

        q2 = deque()

        while len(self.queue) > 1:
            self.q2.appendleft(self.queue.pop())

        val = self.queue.pop()
        self.queue = q2
        return val

    def top(self) -> int:
        if len(self.queue) == 0:
            raise "EMPTY"

        q2 = deque()

        while len(self.queue) > 1:
            self.q2.appendleft(self.queue.pop())

        val = self.queue.pop()
        q2.appendleft(val)
        self.queue = q2
        return val

    def empty(self) -> bool:
        return len(self.queue) == 0
