class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []

        def inorder(root):
            if root.left:
                inorder(root.left)
            result.append(root.val)
            if root.right:
                inorder(root.right)
        inorder(root)
        return result
