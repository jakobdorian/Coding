class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.res = None

        # define a recursive helper function to perform depth-first search
        def dfs(node):
            # base case: if the node is None, return False
            if not node:
                return False
            # recursively traverse the left and right subtrees
            left = dfs(node.left)
            right = dfs(node.right)
            # check if the current node is either p or q
            curr = node == p or node == q
            # check for conditions where the current node is the lowest common ancestor
            if (left and right) or (curr and right) or (curr and left):
                self.res = node
                return
            # return True if the current node, p, or q is found in the subtree
            return left or right or curr
        dfs(root)
        # return the result, which is the lowest common ancestor
        return self.res
