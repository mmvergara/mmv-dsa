from randoms.dsa import *
from collections import deque

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        avg = {}
        queue = deque([(root,0)])
        
        while queue:
            node,level = queue.pop()

            if level not in avg:
                avg[level] = [node.val,1]
            else:
                avg[level][0],avg[level][1] = avg[level][0]+node.val,avg[level][1]+1

            if node.right:
                queue.appendleft((node.right,level+1))
            if node.left:
                queue.appendleft((node.left,level+1))

        res = [0] * len(avg)

        for l,(s,c) in avg.items():
            res[l] = s / c

        return res





class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        avg = {}
        queue = deque([(root,0)])
        
        while queue:
            node,level = queue.pop()

            if level not in avg:
                avg[level] = [node.val,1]
            else:
                avg[level][0],avg[level][1] = avg[level][0]+node.val,avg[level][1]+1

            queue.appendLeft((node.right,leve+1))
            queue.appendLeft((node.right,leve+1))

        res = [0] * len(avg)

        for l,(s,c) in avg.items():
            res[l] = s / c

        return res





