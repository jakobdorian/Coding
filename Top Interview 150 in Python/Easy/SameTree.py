# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# O(p + q) complex
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # check if both trees are empty
        if not p and not q:
            return True
        # check if one of them are empty
        if not p or not q:
            return False
        # check if the tree roots are the same
        if p.val != q.val:
            return False

        # recursive step
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

            