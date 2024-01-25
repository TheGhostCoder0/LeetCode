class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l = []
        if root is None:
            return l
        l += self.inorderTraversal(root.left)
        l.append(root.val)
        l += self.inorderTraversal(root.right)
        return l
