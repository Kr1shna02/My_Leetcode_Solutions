# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        queue = []
        queue.append(root)
        c=1
        while len(queue) != 0:
            value = []
            l = len(queue)
            for _ in range(l):
                a = queue.pop(0)
                if a:
                    value.append(a.val)
                    if a.left:
                        queue.append(a.left)
                    else:
                        queue.append(None)  
                    if a.right:
                        queue.append(a.right)
                    else:
                        queue.append(None)  
                else:
                    value.append("Null")
            if c==1 and len(value)==0:
                c-=1
            if c==0 and len(value)%2!=1:
                return False
            if len(value)%2==0:
                if value[0:]!=value[::-1]:
                    return False
        return True
