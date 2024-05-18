# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return root
        right=[]
        queue=[]
        queue.append(root)
        while len(queue)!=0:
            right.append(queue[-1].val)
            l=len(queue)
            for _ in range(l):
                a=queue.pop(0)
                if a.left:
                    queue.append(a.left)
                if a.right:
                    queue.append(a.right)
        return right
        
