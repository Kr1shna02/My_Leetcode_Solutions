class Solution:
    def __init__(self):
        self.result=[]
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        if root.left:
            self.postorderTraversal(root.left)
        if root.right:
            self.postorderTraversal(root.right)
        self.result.append(root.val)
        return self.result
