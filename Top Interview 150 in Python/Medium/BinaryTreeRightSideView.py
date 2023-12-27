# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # dictionary to store nodes at each height during DFS traversal
        lookup = defaultdict(list)

        def dfs(node, height):
            # base case: if the node is None, return 0
            if not node:
                return 0 

            # append the node value to the list corresponding to its height in the dictionary
            lookup[height].append(node.val)

            # recursively explore the left and right subtrees, incrementing the height
            dfs(node.left, height + 1)
            dfs(node.right, height + 1)

        # perform DFS traversal starting from the root with height 0
        dfs(root, 0)

        # return a list of the last node values at each height, sorted by height
        return [v[-1] for k, v in sorted(lookup.items())]
        