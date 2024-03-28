class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # check if the root is None (empty tree)
        if not root:
            return 0
        
        # recursively calculate the maximum depth of the left and right subtrees,
        # then return the maximum depth among them and add 1 for the current node.
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
