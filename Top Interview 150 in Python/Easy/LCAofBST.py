# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # initialize the current node to the root of the tree
        curr = root

        # traverse the tree until a common ancestor is found
        while curr:
            # if both nodes are greater than the current node, move to the right subtree
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            # if both nodes are smaller than the current node, move to the left subtree
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            # if one node is greater and the other is smaller, the current node is the common ancestor
            else:
                return curr
                