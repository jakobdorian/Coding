# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 1
        self.res = None

        # helper function to perform in-order traversal
        def inOrder(node):
            # base case
            if not node:
                return 0
            
            # recursively traverse left subtree
            inOrder(node.left)
            
            # check if the current node is the kth smallest
            if self.count == k:
                self.res = node.val
            
            # increment the count and recursively traverse right subtree
            self.count += 1
            inOrder(node.right)
            
        inOrder(root)
        return self.res
