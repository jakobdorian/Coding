# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # helper in-order dfs
        def dfs(node, currSum):
            # edge cases
            if not node:
                return False
            
            currSum += node.val
            # check if node is a leaf node (no children)
            if not node.left and not node.right:
                # make sure current sum doesnt exceed target
                return currSum == targetSum
            # recursively run on both sides
            return (dfs(node.left, currSum) or dfs(node.right, currSum))
        return dfs(root, 0)
