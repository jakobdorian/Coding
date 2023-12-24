# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# the time complexity of the code is O(N), where N is the number of nodes in the binary tree. This is because the code performs a depth-first search (DFS) traversal of the entire tree, visiting each node once.

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # initialize a list to store the maximum path sum as a mutable value
        res = [root.val]

        # helper function to perform depth-first search (DFS)
        def dfs(root):
            # Base case: if the current node is None, return 0
            if not root:
                return 0
        
            # recursively calculate the maximum path sum for the left subtree
            leftMax = dfs(root.left)
            
            # recursively calculate the maximum path sum for the right subtree
            rightMax = dfs(root.right)

            # ensure that negative values are treated as 0 (max(0, leftMax))
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # update the global maximum path sum if a better path is found
            res[0] = max(res[0], root.val + leftMax + rightMax)

            # return the maximum path sum starting from the current node
            return root.val + max(leftMax, rightMax)

        # call the DFS function to traverse the tree and calculate the result
        dfs(root)
        
        # return the final result, which is stored in the res list
        return res[0]
