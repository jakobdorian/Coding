# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    prev = float("inf")
    res = float("inf")
    
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # recursive function to perform depth-first search (DFS) on the binary search tree
        def dfs(node):
            # base case
            if not node:
                return 0
            
            # traverse the left subtree if it exists
            if node.left:
                dfs(node.left)
        
            # update the result with the minimum absolute difference between the previous value and the current node's value
            self.res = min(self.res, abs(self.prev - node.val))
        
            # update the previous value to the current node's value
            self.prev = node.val
        
            # traverse the right subtree if it exists
            if node.right:
                dfs(node.right)

        dfs(root)
        return self.res
