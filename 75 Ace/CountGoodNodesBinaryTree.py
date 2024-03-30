class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0

        # dfs function to traverse the tree and count good nodes
        def dfs(node, mx):
            # base case
            if not node:
                return

            # check if the current node is a good node
            if node.val >= mx:
                self.res += 1
            # update the maximum value encountered so far
            mx = max(mx, node.val)
            # Recursively traverse the left and right subtree
            dfs(node.left, mx)
            dfs(node.right, mx)

        # start DFS from the root node with negative infinity as the maximum value
        dfs(root, float("-inf"))

        # return the count of good nodes
        return self.res
