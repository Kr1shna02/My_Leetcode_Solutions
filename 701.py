# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        n=TreeNode(val)
        if not root:
            root=n
            return root
        
        def insert(node,n):
            if node.val>n.val:
                if not node.left:
                    node.left=n
                    return
                insert(node.left,n)
            elif node.val<n.val:
                if not node.right:
                    node.right=n
                    return 
                insert(node.right,n)
        insert(root,n)
        return root

