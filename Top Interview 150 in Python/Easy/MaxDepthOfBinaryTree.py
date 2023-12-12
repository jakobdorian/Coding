# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# recursive DFS sol
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # edge case
        if not root:
           return 0

        # return max sub tree depth
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        