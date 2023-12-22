# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(node):
        # base case: if the node is None, return None for both head and tail
            if not node:
                return None, None

            # recursive call for the left and right subtree
            left, lefttail = dfs(node.left)
            right, righttail = dfs(node.right)
    
            # set the left child of the current node to None (we are modifying the original tree)
            node.left = None
    
            # initialize the end of the circular doubly linked list to the current node
            end = node

            # if there is a left subtree, update the end to connect with it
            if left:
                end.right = left
                end = lefttail

            # if there is a right subtree, update the end to connect with it
            if right:
                end.right = right
                end = righttail

            # return the head and tail of the circular doubly linked list
            return node, end

        # call the dfs function with the root of the binary tree
        dfs(root)
