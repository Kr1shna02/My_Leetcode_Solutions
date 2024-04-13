class Solution:
    def __init__(self):
        self.result=[]
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        if root.left:
            self.inorderTraversal(root.left)
        self.result.append(root.val)
        if root.right:
            self.inorderTraversal(root.right)
        return self.result
