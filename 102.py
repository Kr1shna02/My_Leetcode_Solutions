# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.queue=[]
        self.result=[]
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        self.queue.append(root)
        while len(self.queue)!=0:
            qlen=len(self.queue)
            level=[]
            for i in range(qlen):
                t=self.queue.pop(0)
                level.append(t.val)
                if t.left:
                    self.queue.append(t.left)
                if t.right:
                    self.queue.append(t.right)
            self.result.append(level)
        return self.result
        
        
