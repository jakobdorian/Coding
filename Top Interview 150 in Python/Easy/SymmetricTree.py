# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # recursive helper function
        def dfs(left, right):
            # both nodes are symmetric
            if not left and not right:
                return True
            # only one is symmetric
            if not left or not right:
                return False
            # compare values of nodes
            return (left.val == right.val and dfs(left.left, right.right) and dfs(left. right, right.left))
        
        # call dfs
        return dfs(root.left, root.right)
