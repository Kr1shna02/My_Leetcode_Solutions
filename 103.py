# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res=[]
        self.queue=[]
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        self.queue.append(root)
        j=0
        while len(self.queue)!=0:
            qlen=len(self.queue)
            level=[]
            for i in range(qlen):
                t=self.queue[0]
                level.append(t.val)
                self.queue.pop(0)
                if t.left:
                    self.queue.append(t.left)
                if t.right:
                    self.queue.append(t.right)
            if j%2 == 0:
                self.res.append(level)
            else:
                self.res.append(level[::-1])
            j+=1
        return self.res
