# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # helper function for depth-first search (DFS)
        def dfs(curr, sum):
            # base case: if the current node is None, return 0
            if not curr:
                return 0

            # update the current sum by multiplying it by 10 and adding the current node's value
            sum = sum * 10 + curr.val
            
            # if the current node is a leaf (no left or right children), return the calculated sum
            if not curr.left and not curr.right:
                return sum

            # recursively calculate the sum for the left and right subtrees
            return dfs(curr.left, sum) + dfs(curr.right, sum)

        # start DFS from the root with an initial sum of 0
        return dfs(root, 0)
