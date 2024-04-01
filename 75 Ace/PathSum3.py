class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.res = 0

        # helper function to traverse the tree and find paths
        def helper(node, curr):
            if not node:
                return
            # recursively traverse left and right subtrees
            helper(node.left, curr + node.val)
            helper(node.right, curr + node.val)
            # check if current path sum equals the target sum
            if curr + node.val == targetSum:
                self.res += 1
        
        # dfs function to traverse the tree
        def dfs(node):
            if not node:
                return
            # call helper function to find paths starting from current node
            helper(node, 0)
            # recursively traverse left and right subtrees
            dfs(node.left)
            dfs(node.right)
        
        # start DFS traversal from the root
        dfs(root)
        # return the count of paths
        return self.res
