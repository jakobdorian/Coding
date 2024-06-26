# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        # get a list of nodes in in-order traversal (sorted order)
        nodes = self.inorder_traversal(root)
        # reconstruct the BST from the sorted list of nodes and return the new root
        return self.sorted_bst(nodes, 0, len(nodes) - 1)
        
    def inorder_traversal(self, root: TreeNode) -> list:
        nodes = []
        # helper function to recursively traverse the tree in-order
        def traverse(node):
            if not node:
                return
            traverse(node.left) # traverse the left subtree
            nodes.append(node.val) # visit the current node
            traverse(node.right) # traverse the right subtree
            
        traverse(root)
        return nodes
        
    def sorted_bst(self, nodes: list, start: int, end: int) -> TreeNode:
        # base case: if the start index exceeds the end index, return None (no tree)
        if start > end:
            return None
        
        # find the middle element of the current segment of the list
        mid = (start + end) // 2
        
        # create a new tree node with the middle element as the value
        node = TreeNode(nodes[mid])
        
        # recursively construct the left subtree with the left half of the list
        node.left = self.sorted_bst(nodes, start, mid - 1)
        
        # recursively construct the right subtree with the right half of the list
        node.right = self.sorted_bst(nodes, mid + 1, end)
        
        # return the constructed node
        return node
