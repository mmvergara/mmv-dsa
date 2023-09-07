from randoms.dsa import *


class OrderedStream:
    def __init__(self, n: int):
        self.arr = [None for _ in range(n)]
        self.ptr = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.arr[idKey - 1] = value
        lastptr = self.ptr
        while self.ptr != len(self.arr) and self.arr[self.ptr]:
            self.ptr += 1

        return [self.arr[i] for i in range(lastptr, self.ptr)]
