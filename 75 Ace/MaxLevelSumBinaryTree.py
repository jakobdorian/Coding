class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # empty list to store sums of nodes at each level
        levels = []

        # helper function to traverse the binary tree and calculate sums at each level
        def helper(node, level):
            if not node:
                return
            # if the current level is greater than or equal to the length of levels list, extend the list
            if level >= len(levels):
                levels.append(0)
            # recursively call the helper function for the left and right child nodes
            helper(node.left, level + 1)
            helper(node.right, level + 1)
            # add the value of the current node to the sum of the corresponding level
            levels[level] += node.val

        # call the helper function with root node and level 0 to start the traversal
        helper(root, 0)

        # return the level with the maximum sum of nodes using max() function with a lambda function as key
        # the lambda function sorts based on sum of nodes first and then on level index in descending order
        return max(enumerate(levels), key= lambda x: (x[1], -x[0]))[0] + 1
