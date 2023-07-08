class Node:
    def __init__(self,val=None,left=None,right=None):
        self.val = val
        self.right = right
        self.left = left


class MyHeap:
    # parent ( i - 1 ) / 2
    # right child 2i + 2
    # left child 2i + 1

    def __init__(self):
        self.heap = [4,7,9]
        
    def insert(self,val):
        self.heap.append(val)
        self._siftup(len(self.heap)-1)

    def _siftup(self,i):
        parent = (i-2)//2
        
        # check
        # if i is not 0
        while i != 0 and self.heap[i] < self.heap[parent]:
            # swap parent to the i
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]

            # now the i is in the parent position
            i = parent

            # calculate the new parent index
            parent = (i-2) // 2

    def _siftdown(self,i):

        left = (2*i) + 1
        right = (2*i) + 2

        # first check is if right or left is in boundary
        # 2nd check if current i is greater than left or right subnode
        while (left < len(self.heap) and self.heap[i] > self.heap[left]) or (right <len(self.heap) and self.heap[i] > self.heap[right]):
            
            # initially the smallest is right 
            smallest = right

            # check if right is out of bounds
            # or if left subnode  is smaller than right subnode
            if (right >= len(self.heap) or self.head[left] < self.head[right]):
                smallest = left
            
            # swap values
            self.heap[i], self.heap[smallest] = self.heap[smallest] , self.heap[i]
            
            # Update the current index to the swapped index
            i = smallest 
            
            # Recalculate left and right
            left = (2*i) + 1
            right = (2*i) + 2
 



h = MyHeap()
h.insert(1)
h.insert(0)
print(h.heap)
