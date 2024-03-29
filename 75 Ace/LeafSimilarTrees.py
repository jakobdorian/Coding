class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # dfs function to traverse the tree and collect leaf nodes' values
        def dfs(root, leaf):
            # base case
            if not root:
                return
            # if the current node is a leaf node (no left or right child), append its value to the leaf list
            if not root.left and not root.right:
                leaf.append(root.val)
                return
            # recursively traverse left and right subtrees
            dfs(root.left, leaf)
            dfs(root.right, leaf)

        # lists to store leaf node values for both trees
        leaf1, leaf2 = [], []

        # perform DFS on both trees to collect leaf node values
        dfs(root1, leaf1)
        dfs(root2, leaf2)

        # check if the lists of leaf node values for both trees are identical
        return leaf1 == leaf2
