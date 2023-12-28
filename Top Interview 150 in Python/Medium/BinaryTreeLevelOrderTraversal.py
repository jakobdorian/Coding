# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        hmap = defaultdict(list)

        # helper function to perform depth-first traversal
        def dfs(node, level):
            # base case: if the node is None, return 0
            if not node:
                return 0
            
            # append the value of the current node to the corresponding level in the defaultdict
            hmap[level].append(node.val)

            # recursive calls for the left and right children with an incremented level
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        # start depth-first traversal from the root at level 0
        dfs(root, 0)

        # return the values stored at each level as a list of lists
        return hmap.values()
        