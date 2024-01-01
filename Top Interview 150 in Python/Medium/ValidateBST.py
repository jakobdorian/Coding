# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # helper function for DFS traversal with lower and upper bounds
        def dfs(node, lower, upper):
            # base case: empty node, always valid
            if not node:
                return True
            # check if current node's value violates bounds
            elif node.val <= lower or node.val >= upper:
                return False
            # recursively check left and right subtrees with updated bounds
            else:
                return dfs(node.left, lower, node.val) and dfs(node.right, node.val, upper)
            
        # start DFS traversal from the root with initial bounds as negative infinity and infinity
        return dfs(root, float('-inf'), float('inf'))
        