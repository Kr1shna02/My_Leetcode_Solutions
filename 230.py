# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        data=[]
        def inorder(node):
            if not node:
                return
            if node.left:
                inorder(node.left)
            data.append(node.val)
            if node.right:
                inorder(node.right)
        inorder(root)
        data.sort()
        return data[k-1]
