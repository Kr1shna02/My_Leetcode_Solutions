# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        a=[]
        b=[]
        def preOrder(n,c):
            if not n:
                return 
            c.append(n.val)
            if n.left:
                preOrder(n.left,c)
            else:
                c.append("Null")
            if n.right:
                preOrder(n.right,c)
            else:
                c.append("Null")
        preOrder(p,a)
        preOrder(q,b)
        return a==b
