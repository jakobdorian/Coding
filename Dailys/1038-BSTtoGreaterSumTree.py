# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def reverse_inorder(node: TreeNode, acc:int) -> int:
            if not node:
                return acc
            # process right subtree
            acc = reverse_inorder(node.right, acc)
            # update the current node value
            node.val += acc
            # update the accumlator to the current node val
            acc = node.val
            # process left subtree
            return reverse_inorder(node.left, acc)
        
        reverse_inorder(root, 0)
        return root
        