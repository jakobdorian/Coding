# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# O(n2) sol
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # base case: If the inorder list is empty, return None
        if not inorder:
            return None
        
        # create a new TreeNode with the last element from postorder as the root
        root = TreeNode(postorder.pop())

        # find the index of the root value in the inorder list
        idx = inorder.index(root.val)

        # recursively build the right subtree using elements to the right of the root in inorder and postorder
        root.right = self.buildTree(inorder[idx+1:], postorder)
        
        # recursively build the left subtree using elements to the left of the root in inorder and postorder
        root.left = self.buildTree(inorder[:idx], postorder)

        # return the constructed binary tree
        return root
