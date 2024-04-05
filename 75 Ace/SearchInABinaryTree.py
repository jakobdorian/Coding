class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        curr = root

        # loop until current node is not None
        while curr:
            # if current node's value matches the target value, return current node
            if curr.val == val:
                return curr
            # if current node's value is less than target value, move to the right subtree
            elif curr.val < val:
                curr = curr.right
            # if current node's value is greater than target value, move to the left subtree
            else:
                curr = curr.left
        
        # if target value is not found in the tree, return None
        return None
