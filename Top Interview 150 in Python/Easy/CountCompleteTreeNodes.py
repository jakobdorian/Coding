# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # pre-order dfs O(n) sol
        def dfs(node):
            if not node:
                return 0
            else:
                # return left and right nodes dfs
                return dfs(node.left) + dfs(node.right) + 1
        return dfs(root)
