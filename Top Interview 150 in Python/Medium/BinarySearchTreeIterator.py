# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        """
        constructor for the BSTIterator class.

        parameters:
        - root: Optional[TreeNode]: The root of the binary search tree.

        initializes the stack by pushing all left children of the root onto the stack to start the iteration.
        """
        self.stack = []
        curr = root
        while curr:
            self.stack.append(curr)
            curr = curr.left

    def next(self) -> int:
        """
        returns the next smallest element in the BST.

        if the stack is not empty, pops the top element from the stack and explores its right subtree
        by pushing all left children of the right subtree onto the stack.

        returns:
        - int: The value of the next smallest element.
        """
        if not self.stack:
            return None
        popped = self.stack.pop()
        curr = popped
        if curr.right:
            curr = curr.right
        else:
            curr = None
        while curr:
            self.stack.append(curr)
            curr = curr.left

        return popped.val

    def hasNext(self) -> bool:
        """
        checks if there are more elements in the BST.

        returns:
        - bool: True if there are more elements; False otherwise.
        """
        return self.stack != []

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()