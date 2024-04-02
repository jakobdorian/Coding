class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        # return the maximum length of zigzag paths from left and right subtrees.
        return max(self.helper(root.left, True, 0), self.helper(root.right, False, 0))
    
    # helper function to traverse the binary tree and find zigzag paths.
    def helper(self, root, isLeft, depth):
        if not root:
            return depth

        # if traversing from the left, explore the right subtree first to find the zigzag path.
        if isLeft:
            depth = max(depth, self.helper(root.right, False, depth + 1), 
                        self.helper(root.left, True, 0))
        # if traversing from the right, explore the left subtree first to find the zigzag path.
        else:
            depth = max(depth, self.helper(root.left, True, depth + 1), 
                        self.helper(root.right, False, 0))
        
        return depth
