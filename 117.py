"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        queue=[]
        queue.append(root)
        while len(queue)!=0:
            for i in range(0,len(queue)-1):
                queue[i].next=queue[i+1]
            queue[-1].next=None
            l=len(queue)
            for _ in range(l):
                a=queue[0]
                queue.pop(0)
                if a.left:
                    queue.append(a.left)
                if a.right:
                    queue.append(a.right)
        return root
