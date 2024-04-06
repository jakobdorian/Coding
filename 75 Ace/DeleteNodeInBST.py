class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # base case
        if not root:
            return
        
        # iff the key is greater than the value at the root node, 
        # traverse to the right subtree to find the node to delete.
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        # if the key is smaller than the value at the root node,
        # traverse to the left subtree to find the node to delete.
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            # if the node to delete has no left child, return its right child.
            if not root.left:
                return root.right
            # if the node to delete has no right child, return its left child.
            elif not root.right:
                return root.left
            
            # if the node to delete has both left and right children,
            # find the inorder successor (smallest node in the right subtree).
            curr = root.right
            while curr.left:
                curr = curr.left
            # copy the value of the inorder successor to the node to delete.
            root.val = curr.val
            # delete the inorder successor node from the right subtree.
            root.right = self.deleteNode(root.right, root.val)

        # return the modified root node after deletion.
        return root
        