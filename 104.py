# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue=[]
        queue.append(root)
        count=0
        while len(queue)!=0:
            l=len(queue)
            count+=1
            for _ in range(l):
                a=queue[0]
                queue.pop(0)
                if a.left:
                    queue.append(a.left)
                if a.right:
                    queue.append(a.right)
        return count
